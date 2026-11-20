#!/usr/bin/env python3
"""PCA descritiva EXP-07 em uma coluna de artigo: fonte real auditada.

Reprodução preferida no Google Colab:
  pip install pandas pyarrow scikit-learn matplotlib
  python scripts/figures/gerar_fig02_pca_coluna.py \
      --input features_treino.parquet --output figuras/fig02_pca_coluna.png

A PCA NÃO avalia um classificador nem demonstra generalização.
"""
import argparse
import hashlib
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

SHA_PARQUET = '0a8baa11cee97d338d7a8d92b984f38192ba1a10ec915cc4a06d67ec94ad5c32'
# CSV reconstruído da mesma fonte original, somente para conferir no ambiente sem pyarrow
SHA_CSV_CONFERENCIA = '4ee4bd73ced643d3db107134e5bcc6fb3ae71b2a665f633893e4dc35a8a70dd7'
FEATURES = ['n_tx', 'value_entropy', 'fee_entropy', 'internal_value_entropy', 'call_count_mean']


def gerar(entrada: Path, saida: Path, dpi: int = 450):
    if not entrada.is_file():
        raise FileNotFoundError(entrada)
    sha = hashlib.sha256(entrada.read_bytes()).hexdigest()
    if entrada.suffix.lower() == '.parquet':
        if sha != SHA_PARQUET:
            raise ValueError('Parquet divergente da matriz original auditada: ' + sha)
        d = pd.read_parquet(entrada)
    elif entrada.suffix.lower() == '.csv':
        if sha != SHA_CSV_CONFERENCIA:
            raise ValueError('CSV divergente da cópia local conferida: ' + sha)
        d = pd.read_csv(entrada)
    else:
        raise ValueError('Use arquivo de entrada .parquet (preferível) ou .csv de conferência')
    required = {'recipient', 'dia', 'label', *FEATURES}
    if not required.issubset(d.columns):
        raise ValueError(f'Colunas ausentes: {required - set(d.columns)}')
    if len(d) != 123 or d.label.value_counts().to_dict() != {0: 100, 1: 23}:
        raise ValueError('Quantidade ou composição de classes não coincide com auditoria')
    if d[FEATURES].isna().any().any():
        raise ValueError('A matriz tem features ausentes')
    if d.loc[d.label.eq(1), 'recipient'].nunique() != 1 or d.loc[d.label.eq(0), 'recipient'].nunique() != 100:
        raise ValueError('Composição dos contratos distinta do EXP-07')

    X = StandardScaler().fit_transform(d[FEATURES].astype(float))
    pca = PCA(n_components=2, svd_solver='full')
    pts = pca.fit_transform(X)
    variancia = 100*pca.explained_variance_ratio_
    is_pos = d.label.to_numpy() == 1

    plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':8.1,
                         'axes.spines.top':False, 'axes.spines.right':False})
    fig, ax = plt.subplots(figsize=(3.55,3.45), facecolor='white')
    fig.subplots_adjust(left=.18, right=.955, top=.91, bottom=.285)
    ax.scatter(pts[~is_pos,0], pts[~is_pos,1], s=20, marker='o',
               alpha=.8, edgecolor='white', linewidth=.3,
               label='Negativos · 100 contratos', zorder=2)
    ax.scatter(pts[is_pos,0], pts[is_pos,1], s=28, marker='D',
               alpha=.95, edgecolor='white', linewidth=.45,
               label='Tornado · 1 contrato (23 dias)', zorder=3)
    ax.set_axisbelow(True)
    ax.grid(alpha=.16, linewidth=.55, linestyle='--')
    ax.axhline(0, color='#A4AFB8', linewidth=.55, alpha=.55)
    ax.axvline(0, color='#A4AFB8', linewidth=.55, alpha=.55)
    ax.set_xlabel(f'CP1 · {variancia[0]:.1f}% da variância', labelpad=6)
    ax.set_ylabel(f'CP2 · {variancia[1]:.1f}% da variância', labelpad=7)
    ax.set_title('EXP-07 · PCA das 123 observações', loc='left',
                 fontsize=9.3, fontweight='semibold', pad=7)
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower left', bbox_to_anchor=(.17,.075),
               frameon=False, fontsize=7.7, ncol=1, handletextpad=.65,
               borderpad=0, labelspacing=.45)
    # Apontamento de validade na legenda LaTeX, não na imagem.
    saida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(saida, dpi=dpi, facecolor='white', bbox_inches='tight', pad_inches=.085)
    plt.close(fig)
    print('Figura:', saida.resolve())
    print('Fonte SHA-256:', sha)
    print(f'Variância PC1={variancia[0]:.4f}%, PC2={variancia[1]:.4f}%, total={sum(variancia):.4f}%')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--output', type=Path, default=Path('fig02_pca_coluna.png'))
    p.add_argument('--dpi', type=int, default=450)
    a=p.parse_args()
    gerar(a.input, a.output, a.dpi)
