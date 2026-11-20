#!/usr/bin/env python3
"""Figura 4: EXP-01J — impacto de min_tx na cobertura e na contagem de alertas.

Fonte auditada: comparacao_elegibilidade.csv (EXP-01J, 17/11/2026)
Drive: https://drive.google.com/file/d/1fGYC9pNVHlGILcEbJnlqBqulEWZTM0-o/view

Uso:
  python scripts/figures/gerar_fig04_sensibilidade_exp01j.py \
    --input comparacao_elegibilidade.csv --output fig04_sensibilidade_exp01j.png

Não calcula precision/recall/F1, nem presume que alertas restantes sejam corretos.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, FixedLocator
import pandas as pd

EXPECTED_SHA256 = '8c855262196d5fcadb92ddf9f4c8acc2c8de55b9262ebaf609ffec99623d9b87'
EXPECTED_VALUES = {
  1: (230658, 49, 3),
  5: (7865, 14, 3),
  10: (4038, 9, 3),
  20: (2464, 7, 3),
}


def fmt_br(v):
    return f'{int(v):,}'.replace(',', '.')


def make_figure(input_path: Path, output_path: Path, dpi: int = 350):
    raw = input_path.read_bytes()
    checksum = hashlib.sha256(raw).hexdigest()
    if checksum != EXPECTED_SHA256:
        raise ValueError(f'SHA-256 do CSV não confere: {checksum}')
    df = pd.read_csv(input_path).sort_values('min_tx')
    required = {'min_tx', 'enderecos_unicos', 'alertas', 'pools_artigo_recuperados'}
    if not required.issubset(df.columns):
        raise ValueError(f'Colunas ausentes: {required - set(df.columns)}')
    if len(df) != 4:
        raise ValueError('Esperados quatro cenários EXP-01J.')
    got = {int(r.min_tx): (int(r.enderecos_unicos),int(r.alertas),int(r.pools_artigo_recuperados))
           for r in df.itertuples()}
    if got != EXPECTED_VALUES:
        raise ValueError(f'Valores diferentes dos quatro cenários auditados: {got}')
    if not (df.janelas_elegiveis.equals(df.enderecos_unicos) and
            df.janelas_classificadas.equals(df.enderecos_unicos) and
            df.janelas_invalidadas_por_feature.eq(0).all()):
        raise ValueError('Cobertura da classificação diferente da auditoria EXP-01J.')

    mins = df.min_tx.to_numpy()
    n_eligible = df.enderecos_unicos.to_numpy()
    n_alerts = df.alertas.to_numpy()

    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'axes.spines.top': False, 'axes.spines.right': False})
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10.5, 4.0), facecolor='white')
    fig.subplots_adjust(left=.095, right=.975, top=.77, bottom=.30, wspace=.31)
    # Os dois painéis usam apenas valores de fonte, com escalas diferentes explicitamente.
    ax = axes[0]
    ax.plot(mins, n_eligible, 'o-', linewidth=2.1, markersize=7.5)
    ax.set_yscale('log')
    ax.set_ylim(1500, 450000)
    ax.set_xlim(.4, 20.6)
    ax.set_xticks(mins)
    ax.yaxis.set_major_locator(FixedLocator([2000, 10000, 100000]))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, pos: fmt_br(v)))
    ax.minorticks_off()
    ax.set_xlabel('Mínimo de transações ($min_{tx}$)')
    ax.set_ylabel('Endereços elegíveis (escala log)')
    ax.set_title('(a) Cobertura da classificação', loc='left', fontsize=11.5, pad=11)
    ax.grid(axis='y', linewidth=.7, alpha=.22)
    ax.axvline(10, linewidth=1, linestyle='--', alpha=.35)
    for x,y in zip(mins,n_eligible):
        ax.annotate(fmt_br(y), (x,y), xytext=(0, 10 if x!=5 else -17),
                    textcoords='offset points', ha='center', va='bottom', fontsize=9.7,
                    weight='semibold')

    ax = axes[1]
    ax.plot(mins, n_alerts, 'o-', linewidth=2.1, markersize=7.5)
    ax.set_xlim(.4,20.6)
    ax.set_ylim(0,58)
    ax.set_xticks(mins)
    ax.set_yticks([0,10,20,30,40,50])
    ax.set_xlabel('Mínimo de transações ($min_{tx}$)')
    ax.set_ylabel('Contratos sinalizados')
    ax.set_title('(b) Alertas produzidos', loc='left', fontsize=11.5, pad=11)
    ax.grid(axis='y', linewidth=.7, alpha=.22)
    ax.axvline(10, linewidth=1, linestyle='--', alpha=.35)
    for x,y in zip(mins,n_alerts):
        ax.annotate(str(y),(x,y),xytext=(0,10),textcoords='offset points',
                    ha='center',fontsize=11,weight='bold')

    fig.text(.095,.925,'EXP-01J | Sensibilidade ao filtro mínimo de transações',
             color='#202E3A',fontsize=15,weight='bold')
    fig.text(.095,.85,'Ethereum · 29/10/2020 · mesmo modelo e limiar de decisão (0,5)',
             color='#5D6A79',fontsize=10.5)
    fig.text(.095,.17,'Os 3 pools Tornado Cash de referência foram sinalizados nos quatro cenários.',
             color='#333D47',fontsize=9.7)
    fig.text(.095,.095,'O filtro altera a população avaliada; redução de alertas não demonstra aumento de precisão.',
             color='#5D6A79',fontsize=9.3)
    output_path.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output_path,dpi=dpi,bbox_inches='tight',pad_inches=.12,facecolor='white')
    plt.close(fig)
    print('PNG:',output_path.resolve())
    print('SHA-256 do CSV de entrada:',checksum)
    print('Cenários verificados:',got)
    return got

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,default=Path('fig04_sensibilidade_exp01j.png'))
    p.add_argument('--dpi',type=int,default=350)
    args=p.parse_args()
    make_figure(args.input,args.output,args.dpi)
