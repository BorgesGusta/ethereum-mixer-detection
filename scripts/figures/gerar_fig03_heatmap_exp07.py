#!/usr/bin/env python3
"""Figura 3 -- mapa de calor do EXP-07 com o resumo original auditado.

Reprodução no repositório/Colab:
  python scripts/figures/gerar_fig03_heatmap_exp07.py \
    --input resumo_12_combinacoes.csv --output fig03_heatmap_exp07.png

A figura retrata médias de F1 dos cinco folds estratificados POR LINHAS.
Como há um único contrato positivo, NÃO é um teste de generalização.
Não cria resultados, não reentreina modelos e não infere rótulos novos.
"""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
import numpy as np
import pandas as pd

SHA256_RESUMO = 'f1b2da3a9916c298a3d0731b781955ec05c7defd2f83455163fcf2eb68dda6e6'
MODELS = {
    'RandomForest': 'Random Forest',
    'DecisionTree': 'Árvore de decisão',
    'GradientBoosting': 'Gradient Boosting',
    'RegressaoLogistica': 'Regressão logística',
}
SETS = {
    'A_original_5': 'A — Original\n5 atributos',
    'B_sem_volume_4': 'B — Sem volume\n4 atributos',
    'C_entropias_3': 'C — Entropias\n3 atributos',
}


def make_figure(input_path: Path, output_path: Path, dpi: int = 350):
    if not input_path.is_file():
        raise FileNotFoundError(input_path)
    checksum = hashlib.sha256(input_path.read_bytes()).hexdigest()
    if checksum != SHA256_RESUMO:
        raise ValueError(f'SHA-256 inválido. Recebido {checksum}; esperado {SHA256_RESUMO}')
    d = pd.read_csv(input_path)
    must = {'configuracao', 'modelo', 'f1_mean', 'f1_std'}
    if not must.issubset(d.columns):
        raise ValueError(f'Colunas faltantes: {sorted(must-set(d.columns))}')
    if len(d) != 12 or d[['configuracao','modelo']].duplicated().any():
        raise ValueError('Esperadas exatamente 12 combinações únicas (4 modelos x 3 grupos).')
    if set(d.modelo) != set(MODELS) or set(d.configuracao) != set(SETS):
        raise ValueError('Modelos ou configurações não correspondem ao protocolo EXP-07 v2.')
    vals = d.pivot(index='modelo', columns='configuracao', values='f1_mean')
    vals = vals.loc[list(MODELS), list(SETS)].to_numpy(dtype=float)
    if not np.all(np.isfinite(vals)) or not np.all((vals >= 0) & (vals <= 1)):
        raise ValueError('F1 deve ser numérico entre zero e um.')

    plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10,
                         'axes.spines.top':False, 'axes.spines.right':False})
    fig = plt.figure(figsize=(9.8, 5.0), facecolor='white')
    ax = fig.add_axes([0.22, 0.255, 0.68, 0.475])
    cmap = plt.get_cmap('YlGnBu')
    norm = mcolors.Normalize(vmin=0.50, vmax=1.00)
    im = ax.imshow(vals, cmap=cmap, norm=norm, aspect='auto', interpolation='nearest')
    ax.set_xticks(range(3), [SETS[s] for s in SETS], fontsize=11, fontweight='medium')
    ax.set_yticks(range(4), [MODELS[m] for m in MODELS], fontsize=10.5)
    ax.tick_params(length=0, pad=10)
    ax.xaxis.tick_top()
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_xticks(np.arange(-.5,3,1), minor=True)
    ax.set_yticks(np.arange(-.5,4,1), minor=True)
    ax.grid(which='minor', color='white', linewidth=3)
    ax.tick_params(which='minor', bottom=False, left=False)

    for i in range(4):
        for j in range(3):
            x = vals[i,j]
            rgba = cmap(norm(x))
            lum = (0.2126*rgba[0]+0.7152*rgba[1]+0.0722*rgba[2])
            txt_color = '#FFFFFF' if lum < 0.55 else '#213346'
            ax.text(j, i, f'{x:.4f}'.replace('.',','), ha='center', va='center',
                    color=txt_color, fontsize=14.5, fontweight='bold' if i == 0 else 'medium')

    bar = fig.colorbar(im, ax=ax, orientation='vertical', fraction=.036, pad=.023,
                       shrink=0.96, ticks=[0.5,0.6,0.7,0.8,0.9,1.0])
    bar.ax.tick_params(labelsize=8.5, length=0)
    bar.ax.set_yticklabels(['0,5','0,6','0,7','0,8','0,9','1,0'])
    bar.set_label('F1 médio interno', fontsize=9.5, labelpad=12)
    bar.outline.set_visible(False)

    fig.text(.055, .962, 'Comparação de classificadores e ablação — EXP-07',
             fontsize=16, weight='bold', color='#1E334A', va='top')
    fig.text(.055, .903, '12 combinações · cinco folds estratificados por linhas · mesma matriz rotulada',
             fontsize=10.5, color='#4B5F71', va='top')
    fig.add_artist(plt.Line2D([.055,.945],[.185,.185], transform=fig.transFigure,
                              color='#D7E1E9', linewidth=1.0))
    fig.text(.055, .142, 'AVALIAÇÃO EXPLORATÓRIA', fontsize=9.7,
             color='#9D603B', weight='bold', va='center')
    fig.text(.055, .095,
             'Os 23 positivos pertencem a um único contrato, presente no treino e na validação dos cinco folds.',
             fontsize=9.65, color='#3A4758', va='center')
    fig.text(.055, .055, 'F1 interno não demonstra detecção de contratos ou protocolos inéditos.',
             fontsize=9.55, color='#3A4758', va='center')

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi, facecolor='white', bbox_inches='tight', pad_inches=.14)
    plt.close(fig)
    print('PNG:', output_path.resolve())
    print('SHA-256 CSV:', checksum)
    print('Matriz F1 (linhas RF, DT, GB, RL; colunas A, B, C):')
    print(vals)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--input', type=Path, required=True, help='CSV oficial resumo_12_combinacoes.csv')
    p.add_argument('--output', type=Path, default=Path('fig03_heatmap_exp07.png'))
    p.add_argument('--dpi', type=int, default=350)
    a = p.parse_args()
    make_figure(a.input, a.output, a.dpi)
