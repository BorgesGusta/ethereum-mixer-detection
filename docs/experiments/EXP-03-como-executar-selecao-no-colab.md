# EXP-03 — Executar apenas a seleção de controles no Colab

**Criado:** 18/11/2026. **Estado: execução REAL ainda pendente.** Não execute os notebooks EXP-02B/02C novamente. Não há nova coleta de transações nem treinamento nesta etapa.

## Por que não foi executado nesta sessão

O ambiente local permite baixar arquivos do Drive, mas não possui biblioteca `pyarrow` para abrir Parquet; a tentativa de instalação foi bloqueada por indisponibilidade de rede. Esta limitação é do **ambiente de execução**, não prova de defeito dos arquivos. Os três insumos foram encontrados no Drive oficial, inclusive modelo de 98.089 bytes e features 2026 de 12.591.717 bytes. A reexecução do notebook 07b inteiro seria retrabalho.

## Entrada congelada e código versionado

| Origem | Arquivo | ID do Drive |
|---|---|---|
| `data/processed` | `features_2026-01-15.parquet` | `12NHTZGd_-RPIt6c2gYlEjO0WZHcfyqQl` |
| `data/processed` | `modelo_rf.joblib` | `1nFKrY4P0hVb5tVspMyNLZMGzltcKZh2x` |
| `results` | `sinalizados_teste_2026.csv` | `11kWohs3VvdDGVjwsN_t-S8EQVix6n9mf` |
| `results` | `limiar_congelado_2026.json` | `1rVq1bPOvy1pxtQVmuXOFKecfGcFRPd_d` (conferido: 0,85) |

Script novo: [`scripts/exp03_selecionar_controles.py`](../../scripts/exp03_selecionar_controles.py). O script reproduz **apenas os scores**, não executa um novo experimento de avaliação temporal.

## Uma célula no Colab (não criar notebook canônico novo)

Abra um Colab Python temporário, use sua conta autorizada no Drive oficial e execute **esta única célula**. Ela baixa apenas três arquivos já existentes (~13 MB), fixa a versão do script no commit indicado, não acessa dados privados fora da pasta do projeto e salva saídas em pasta nova no Drive.

```python
%pip -q install pyarrow joblib scikit-learn pandas requests

from google.colab import auth
auth.authenticate_user()
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from pathlib import Path
from datetime import datetime, timezone
import io, requests, subprocess, sys

api = build("drive", "v3")
base = Path("/content/EXP03_selecao")
base.mkdir(exist_ok=True)
ids = {
    "features_2026-01-15.parquet": "12NHTZGd_-RPIt6c2gYlEjO0WZHcfyqQl",
    "modelo_rf.joblib": "1nFKrY4P0hVb5tVspMyNLZMGzltcKZh2x",
    "sinalizados_teste_2026.csv": "11kWohs3VvdDGVjwsN_t-S8EQVix6n9mf",
}
for name, file_id in ids.items():
    target = base/name
    req = api.files().get_media(fileId=file_id)
    with target.open("wb") as f:
        loader = MediaIoBaseDownload(f, req)
        done = False
        while not done:
            _, done = loader.next_chunk()
    print("Entrada obtida:", name, target.stat().st_size)

commit = "360d351962ef7aff7db7dc957fbeecbd182058df"
script_url = (f"https://raw.githubusercontent.com/BorgesGusta/"
              f"ethereum-mixer-detection/{commit}/scripts/exp03_selecionar_controles.py")
response = requests.get(script_url, timeout=45)
response.raise_for_status()
script = base/"exp03_selecionar_controles.py"
script.write_bytes(response.content)
out = base/"saida"
cmd = [sys.executable, str(script), "--features", str(base/"features_2026-01-15.parquet"),
       "--modelo", str(base/"modelo_rf.joblib"), "--ranking",
       str(base/"sinalizados_teste_2026.csv"), "--saida", str(out)]
subprocess.run(cmd, check=True)

# Só faz upload caso todas as travas de paridade tenham sido satisfeitas.
results_parent = "1iZKAeZPEb6JOlH8KfqsR6-wqI1ygmojI"
folder_name = "EXP-03_selecao_controles_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
folder = api.files().create(
    body={"name":folder_name, "mimeType":"application/vnd.google-apps.folder",
          "parents":[results_parent]}, fields="id,name"
).execute()
for p in sorted(out.iterdir()):
    uploaded = api.files().create(
        body={"name":p.name,"parents":[folder["id"]]},
        media_body=MediaFileUpload(str(p), mimetype="text/csv" if p.suffix==".csv" else "application/json",
                                   resumable=True),
        fields="id,name"
    ).execute()
    print("Salvo:", uploaded["name"], uploaded["id"])
print("PASTA DE RESULTADOS:", "https://drive.google.com/drive/folders/"+folder["id"])
```

## Gates/checagens

- Se os elegíveis não forem exatamente **20.214**, **ABORTAR**.
- Se não reproduzir os **mesmos nove endereços** com `score > 0,85`, **ABORTAR**.
- Se o score original dos nove alertas divergir em mais de 1e-8, **ABORTAR**.
- Se não houver seis controles únicos pareados em `n_tx`, **ABORTAR**.
- Os seis controles gerados ainda são **candidatos provisórios**: não há garantia de que sejam contratos em vez de EOAs. A checagem de contrato e atividade histórica faz parte da fase seguinte, antes da auditoria comparativa.
- Não publicar precision, recall ou F1 nem denominar controles como negativos verdadeiros.

## Saídas previstas, ainda não existentes

- `controles_provisorios.csv`: seis pares e respectivas faixas de atividade, scores e pendência de verificação do tipo de endereço.
- `manifesto_selecao.json`: SHA-256 dos três insumos, paridade dos nove alertas, limiar, critério de escolha, registro da execução e SHA-256 da saída.

**Após executar:** registrar URL da pasta nova do Drive e conferir os hashes na sessão seguinte; somente então marcar D1.9 como seleção congelada e avaliar consultas externas de EXP-03. Não marcar a tarefa como concluída pela existência deste procedimento.
