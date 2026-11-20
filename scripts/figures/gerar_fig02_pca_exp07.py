#!/usr/bin/env python3
"""Figura 2: PCA exploratória das cinco características da matriz REAL EXP-07.

Reprodução canônica (Colab/terminal):
  pip install pandas pyarrow scikit-learn matplotlib
  python gerar_fig02_pca_exp07.py --input features_treino.parquet --output fig02_pca_exp07.png

No ambiente offline de conferência, foi usado CSV decodificado da MESMA matriz
Parquet de SHA-256 fixo; esta opção NÃO constitui outra amostra:
  python gerar_fig02_pca_exp07.py --input features_treino_reconstructed_local.csv

A PCA é ajustada em todas as 123 linhas, exclusivamente para visualização.
Não é avaliação de classificador nem prova de generalização.
"""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

EXPECTED_PARQUET_SHA256 = '0a8baa11cee97d338d7a8d92b984f38192ba1a10ec915cc4a06d67ec94ad5c32'
FEATURES = ['n_tx', 'value_entropy', 'fee_entropy', 'internal_value_entropy', 'call_count_mean']


def make_figure(input_path: Path, output_path: Path, dpi: int = 350):
    if not input_path.is_file():
        raise FileNotFoundError(input_path)
    if input_path.suffix.lower() == '.parquet':
        h = hashlib.sha256(input_path.read_bytes()).hexdigest()
        if h != EXPECTED_PARQUET_SHA256:
            raise RuntimeError(f'SHA256 da matriz incorreto: {h}; esperado {EXPECTED_PARQUET_SHA256}')
        df = pd.read_parquet(input_path)
    elif input_path.suffix.lower() == '.csv':
        print('AVISO: CSV alternativo. Confira sua origem no Parquet canônico do EXP-07.')
        df = pd.read_csv(input_path)
    else:
        raise ValueError('Use .parquet (preferível) ou .csv.')
    required = ['recipient', 'label', 'dia', *FEATURES]
    missing = set(required) - set(df.columns)
    if missing:
        raise RuntimeError(f'Faltam colunas {sorted(missing)}')
    if df.shape[0] != 123 or df.label.value_counts().to_dict() != {0: 100, 1: 23}:
        raise RuntimeError('A matriz não corresponde à composição auditada do EXP-07.')
    if df[FEATURES].isna().any().any():
        raise RuntimeError('Existem valores ausentes nas cinco características.')
    distinct_pos = df.loc[df.label.eq(1), 'recipient'].nunique()
    distinct_neg = df.loc[df.label.eq(0), 'recipient'].nunique()
    if (distinct_pos, distinct_neg) != (1, 100):
        raise RuntimeError(f'Contratos distintos inesperados: {distinct_pos} positivos / {distinct_neg} negativos.')

    X = StandardScaler().fit_transform(df[FEATURES].astype(float))
    pca = PCA(n_components=2, svd_solver='full')
    proj = pca.fit_transform(X)
    exp = pca.explained_variance_ratio_ * 100

    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10.5,
                         'axes.spines.top': False, 'axes.spines.right': False})
    fig, ax = plt.subplots(figsize=(8.7, 4.8))
    fig.patch.set_facecolor('white')
    fig.subplots_adjust(left=0.095, right=0.965, top=0.88, bottom=0.22)
    mask = df.label.to_numpy() == 1
    cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
    c0, c1 = cycle[0], cycle[1]
    ax.scatter(proj[~mask, 0], proj[~mask, 1], s=39, c=c0, alpha=0.75,
               edgecolors='white', linewidths=0.35, marker='o',
               label=f'Não mixer: 100 observações / {distinct_neg} contratos', zorder=2)
    ax.scatter(proj[mask, 0], proj[mask, 1], s=60, c=c1, alpha=0.95,
               edgecolors='white', linewidths=0.65, marker='D',
               label=f'Tornado Cash: 23 dias / {distinct_pos} contrato', zorder=3)
    ax.axhline(0, color='#D3DCE4', lw=0.8, zorder=0)
    ax.axvline(0, color='#D3DCE4', lw=0.8, zorder=0)
    ax.grid(alpha=0.12, linestyle='--', linewidth=0.65, zorder=0)
    ax.set_axisbelow(True)
    ax.set_xlabel(f'Componente principal 1 ({exp[0]:.1f}% da variância)', labelpad=8)
    ax.set_ylabel(f'Componente principal 2 ({exp[1]:.1f}% da variância)', labelpad=8)
    ax.set_title('Distribuição dos exemplos rotulados — EXP-07', loc='left',
                 fontsize=13, weight='semibold', pad=14)
    leg = ax.legend(loc='upper right', frameon=True, fancybox=False, fontsize=9.2,
                    facecolor='white', edgecolor='#D5DEE7')
    leg.get_frame().set_alpha(0.96)
    fig.text(0.10, 0.095,
             'Projeção exploratória das 5 características padronizadas. '
             'As 23 observações positivas são do mesmo contrato.',
             fontsize=9.2, color='#485665')
    fig.text(0.10, 0.057,
             'Não representa validação independente, detecção de anomalias ou grafo de transações.',
             fontsize=9.0, color='#485665')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi, facecolor='white')
    plt.close(fig)
    print(f'PNG: {output_path.resolve()}')
    print(f'PCA: CP1={exp[0]:.4f}% CP2={exp[1]:.4f}% Total={sum(exp):.4f}%')
    print(f'Composição: classe 0={len(df)-mask.sum()}, classe 1={mask.sum()}, '
          f'contratos positivos={distinct_pos}, negativos={distinct_neg}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', type=Path, default=Path('features_treino.parquet'))
    ap.add_argument('--output', type=Path, default=Path('fig02_pca_exp07.png'))
    ap.add_argument('--dpi', type=int, default=350)
    args = ap.parse_args()
    make_figure(args.input, args.output, args.dpi)
