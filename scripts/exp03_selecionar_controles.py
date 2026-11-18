"""EXP-03: seleção exploratória de controles sem consultas externas e sem retreino.

Entradas oficiais: features_2026-01-15.parquet, modelo_rf.joblib e
sinalizados_teste_2026.csv do Drive; limiar previamente congelado 0.85.

Não executa auditoria de blockchain, não estima precisão nem afirma ground truth.
Abortar se a reprodução do ranking original não for EXATA por identidade.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

FEATURES = ["value_entropy", "fee_entropy", "internal_value_entropy", "call_count_mean"]
BANDS = [(10, 19), (20, 49), (50, 99), (100, None)]
THRESHOLD = 0.85
DAY = "2026-01-15"
SEED_LABEL = "EXP03-20261118|"
EXPECTED_ELIGIBLE = 20214
EXPECTED_ALERTS = 9


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def band(n: int) -> int:
    for i, (lo, hi) in enumerate(BANDS):
        if n >= lo and (hi is None or n <= hi):
            return i
    raise ValueError(f"n_tx fora de banda elegível: {n}")


def choose_controls(alerts: pd.DataFrame, eligible: pd.DataFrame) -> pd.DataFrame:
    """Emparelhar 6 alertas não-referência: banda igual; fallback banda adjacente."""
    candidates = eligible.loc[~eligible["alerta"]].copy()
    # Ordenação sem avaliar nomes, identidade econômica ou eventos on-chain.
    candidates["ordem_cego"] = candidates["recipient"].map(
        lambda addr: hashlib.sha256((SEED_LABEL + addr).encode()).hexdigest()
    )
    candidates["banda"] = candidates["n_tx"].astype(int).map(band)
    alerts = alerts.copy()
    alerts["banda"] = alerts["n_tx"].astype(int).map(band)
    chosen = []
    used = set()
    for row in alerts.sort_values(["recipient"]).itertuples(index=False):
        # Fallback rígido: banda de distância 0, depois 1, 2, 3.
        pool = candidates.loc[~candidates["recipient"].isin(used)].copy()
        pool["distancia_banda"] = (pool["banda"] - row.banda).abs()
        pool = pool.sort_values(
            ["distancia_banda", "ordem_cego", "recipient"], kind="mergesort"
        )
        if pool.empty:
            continue
        c = pool.iloc[0]
        used.add(c["recipient"])
        chosen.append(
            {
                "alertado": row.recipient,
                "n_tx_alertado": int(row.n_tx),
                "score_alertado": float(row.prob),
                "controle_candidato": c["recipient"],
                "n_tx_controle": int(c["n_tx"]),
                "score_controle": float(c["prob"]),
                "banda_alertado": int(row.banda),
                "banda_controle": int(c["banda"]),
                "distancia_banda": int(c["distancia_banda"]),
                "contrato_controle_historicamente_confirmado": False,
                "status": "provisorio_aguardando_verificacao_tipo_de_endereco",
            }
        )
    return pd.DataFrame(chosen)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--features", type=Path, required=True)
    ap.add_argument("--modelo", type=Path, required=True)
    ap.add_argument("--ranking", type=Path, required=True)
    ap.add_argument("--saida", type=Path, required=True)
    args = ap.parse_args()

    if args.saida.exists() and any(args.saida.iterdir()):
        raise RuntimeError("Diretório de saída não vazio: não sobrescrever resultados.")
    if not all(p.is_file() for p in [args.features, args.modelo, args.ranking]):
        raise FileNotFoundError("Entradas ausentes; usar cópias oficiais do Drive.")

    # joblib contém objetos pickle: só carregar modelo conhecido e confiável do projeto.
    df = pd.read_parquet(args.features)
    old = pd.read_csv(args.ranking, dtype={"recipient": str})
    needed = {"recipient", "n_tx", "rotulo", *FEATURES}
    absent = needed - set(df.columns)
    if absent:
        raise ValueError(f"Colunas ausentes: {sorted(absent)}")
    if not {"recipient", "prob", "n_tx"}.issubset(old.columns):
        raise ValueError("Ranking legado sem recipient/prob/n_tx.")
    df["recipient"] = df["recipient"].astype(str).str.lower()
    old["recipient"] = old["recipient"].astype(str).str.lower()
    if df["recipient"].duplicated().any() or old["recipient"].duplicated().any():
        raise ValueError("Duplicatas de endereço em features ou ranking legado.")
    eligible = df.loc[(df["n_tx"] >= 10) & df["rotulo"].ne("router")].copy()
    if len(eligible) != EXPECTED_ELIGIBLE:
        raise RuntimeError(
            f"Elegíveis {len(eligible)} != {EXPECTED_ELIGIBLE}: ABORTAR, não escolher controles."
        )
    if eligible[FEATURES].isna().any().any():
        raise RuntimeError("Features com NaN; ABORTAR em vez de imputar silenciosamente.")
    model = joblib.load(args.modelo)
    # O modelo deve possuir estas features na ordem exata e classes binárias.
    if list(getattr(model, "classes_", [])) != [0, 1]:
        raise RuntimeError("Classes do modelo inesperadas.")
    if hasattr(model, "feature_names_in_") and list(model.feature_names_in_) != FEATURES:
        raise RuntimeError("Ordem de features incompatível.")
    eligible["prob"] = model.predict_proba(eligible[FEATURES])[:, 1]
    eligible["alerta"] = eligible["prob"] > THRESHOLD
    got = eligible.loc[eligible["alerta"], ["recipient", "prob"]]
    if len(got) != EXPECTED_ALERTS or set(got["recipient"]) != set(old["recipient"]):
        raise RuntimeError("Falha de paridade: os nove alertas legados não foram reproduzidos.")
    original_scores = old.set_index("recipient")["prob"].astype(float)
    current_scores = got.set_index("recipient")["prob"].astype(float)
    maxdiff = float((current_scores - original_scores).abs().max())
    if not np.isclose(maxdiff, 0, atol=1e-8):
        raise RuntimeError(f"Scores dos nove alertas divergiram: {maxdiff}. ABORTAR.")

    # Todos os endereços alertados fora dos três pools conhecidos serão casos já estudados.
    tornado = {"0.1 ETH", "1 ETH", "10 ETH"}
    cases = old.loc[~old["rotulo"].isin(tornado), "recipient"]
    if len(cases) != 6:
        raise RuntimeError("Esperados seis alertas adicionais; não ajustar amostra.")
    alert_cases = eligible.loc[eligible["recipient"].isin(cases)]
    if len(alert_cases) != 6:
        raise RuntimeError("Casos adicionais não encontrados entre os elegíveis.")
    pairs = choose_controls(alert_cases, eligible)
    if len(pairs) != 6 or pairs["controle_candidato"].nunique() != 6:
        raise RuntimeError("Não foi possível selecionar seis controles únicos.")

    # Arquivos só depois de todas as travas de paridade acima.
    args.saida.mkdir(parents=True, exist_ok=True)
    pairs.to_csv(args.saida / "controles_provisorios.csv", index=False)
    metadata = {
        "experimento": "EXP-03_preparacao",
        "fase": "selecao_de_controles_sem_consultas_externas",
        "status": "controles_provisorios_sem_verificacao_historica",
        "executado_utc": datetime.now(timezone.utc).isoformat(),
        "dia_bloco": DAY,
        "threshold_original": THRESHOLD,
        "min_tx_original": 10,
        "referencia_n_elegiveis": EXPECTED_ELIGIBLE,
        "referencia_n_alertas": EXPECTED_ALERTS,
        "paridade_identidades_alertas": True,
        "diferenca_maxima_scores_alertas": maxdiff,
        "criterio_selecao": "mesma banda de n_tx; fallback menor distancia ordinal; SHA256 salgado por endereco",
        "bandas": ["10-19", "20-49", "50-99", "100+"],
        "entradas_sha256": {
            "features": sha256_file(args.features),
            "modelo": sha256_file(args.modelo),
            "ranking_legado": sha256_file(args.ranking),
        },
        "avisos": [
            "Dados de 2026 ja explorados; resultado nao e holdout cego.",
            "Controles selecionados ainda podem ser EOAs; tipo e funcao devem ser verificados antes da auditoria comparativa.",
            "Nao sao rotulos negativos confirmados e nao autorizam precision/recall/F1.",
            "Sem treinamento, calibragem, mudanca de limiar ou coleta externa.",
        ],
    }
    metadata["sha256_saida"] = sha256_file(args.saida / "controles_provisorios.csv")
    (args.saida / "manifesto_selecao.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print("PARIDADE OK: 20214 elegiveis, 9 alertas originais, 6 pares provisorios")
    print(f"SHA256 resultados: {metadata['sha256_saida']}")


if __name__ == "__main__":
    main()
