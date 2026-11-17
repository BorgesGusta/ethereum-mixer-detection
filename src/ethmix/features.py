"""Compatibilidade de features com notebook legado 03_v2 (não altera datasets)."""
import numpy as np
import pandas as pd

FEATURES = ("value_entropy", "fee_entropy", "internal_value_entropy", "call_count_mean")
DECIMAIS = {"value_eth": 4, "fee_eth": 6, "internal_value_eth": 4}

def preparar(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza colunas de transações em wei/ETH e datas UTC."""
    df = df.copy()
    for c in ("value", "internal_value", "fee"):
        if c + "_eth" not in df:
            if c not in df:
                raise KeyError(f"Ausente: {c} ou {c}_eth")
            df[c + "_eth"] = pd.to_numeric(df[c], errors="coerce") / 1e18
    df["time"] = pd.to_datetime(df["time"], utc=True)
    df["dia"] = df["time"].dt.date
    df["recipient"] = df["recipient"].astype(str).str.lower()
    df["call_count"] = pd.to_numeric(df["call_count"], errors="coerce")
    return df[["hash", "time", "dia", "sender", "recipient", "call_count",
               "value_eth", "internal_value_eth", "fee_eth"]]

def entropia(df: pd.DataFrame, chaves, col, decimais):
    """Shannon base 2; agrupa incluindo nulos, como notebook 03_v2."""
    chaves = list(chaves)
    v = pd.to_numeric(df[col], errors="coerce").round(decimais)
    cont = df.assign(_v=v).groupby(chaves+["_v"], observed=True, dropna=False).size()
    p = cont/cont.groupby(level=chaves).transform("sum")
    return (-(p*np.log2(p))).groupby(level=chaves).sum()

def calcular_features(df: pd.DataFrame, chaves=("recipient", "dia")) -> pd.DataFrame:
    chaves=list(chaves)
    g=df.groupby(chaves, observed=True)
    saida=pd.DataFrame({
        "n_tx":g.size(),
        "value_entropy":entropia(df,chaves,"value_eth",DECIMAIS["value_eth"]),
        "fee_entropy":entropia(df,chaves,"fee_eth",DECIMAIS["fee_eth"]),
        "internal_value_entropy":entropia(df,chaves,"internal_value_eth",DECIMAIS["internal_value_eth"]),
        "call_count_mean":g["call_count"].mean()
    })
    return saida.reset_index()
