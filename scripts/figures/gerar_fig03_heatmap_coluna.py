#!/usr/bin/env python3
"""Heatmap EXP-07 de UMA coluna, reproduzido do CSV oficial com SHA-256.

Uso:
  python scripts/figures/gerar_fig03_heatmap_coluna.py \
    --input resumo_12_combinacoes.csv \
    --output figuras/fig03_heatmap_coluna.png

Médias do F1 de cinco folds por LINHA (mesmo contrato positivo em treino/teste).
NÃO constitui generalização a novos contratos ou protocolos.
"""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

EXPECTED_SHA = 'f1b2da3a9916c298a3d0731b781955ec05c7defd2f83455163fcf2eb68dda6e6'
MODELS = [('RandomForest','Random Forest'),('DecisionTree','Árvore decisão'),
          ('GradientBoosting','Grad. Boosting'),('RegressaoLogistica','Reg. logística')]
SETS = [('A_original_5','A'),('B_sem_volume_4','B'),('C_entropias_3','C')]

def gerar(entrada: Path, saida: Path, dpi: int = 450):
    if not entrada.is_file(): raise FileNotFoundError(entrada)
    checksum = hashlib.sha256(entrada.read_bytes()).hexdigest()
    if checksum != EXPECTED_SHA:
        raise ValueError('CSV diferente do resumo auditado EXP-07: ' + checksum)
    d = pd.read_csv(entrada)
    required = {'configuracao','modelo','f1_mean','f1_std'}
    if not required.issubset(d.columns):
        raise ValueError('Colunas ausentes: '+str(required-set(d.columns)))
    if len(d)!=12 or d[['configuracao','modelo']].duplicated().any():
        raise ValueError('Esperadas 12 combinações únicas')
    if set(d['modelo'])!={k for k,_ in MODELS} or set(d['configuracao'])!={k for k,_ in SETS}:
        raise ValueError('Modelo ou conjunto diferente do protocolo EXP-07')
    mat=d.pivot(index='modelo',columns='configuracao',values='f1_mean')
    mat=mat.loc[[k for k,_ in MODELS],[k for k,_ in SETS]].to_numpy(dtype=float)
    if not np.isfinite(mat).all() or not ((mat>=0)&(mat<=1)).all():
        raise ValueError('F1 inválido')

    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8.0})
    fig = plt.figure(figsize=(3.55,3.00),facecolor='white')
    ax = fig.add_axes([.395,.295,.56,.475])
    cmap=plt.get_cmap('YlGnBu')
    norm=Normalize(.5,1.0)
    ax.imshow(mat,cmap=cmap,norm=norm,aspect='auto',interpolation='nearest')
    ax.set_xticks(np.arange(3),[label for _,label in SETS],fontsize=9,weight='medium')
    ax.xaxis.tick_top()
    ax.set_yticks(np.arange(4),[name for _,name in MODELS],fontsize=7.65)
    ax.tick_params(length=0,pad=6)
    ax.set_xticks(np.arange(-.5,3,1),minor=True)
    ax.set_yticks(np.arange(-.5,4,1),minor=True)
    ax.grid(which='minor',color='white',linewidth=2)
    ax.tick_params(which='minor',bottom=False,left=False)
    for s in ax.spines.values(): s.set_visible(False)
    for i in range(4):
        for j in range(3):
            f=mat[i,j]
            rgba=cmap(norm(f))
            bright=.2126*rgba[0]+.7152*rgba[1]+.0722*rgba[2]
            ax.text(j,i,f'{f:.4f}'.replace('.',','),ha='center',va='center',
                    fontsize=7.9,fontweight='bold' if i==0 else 'medium',
                    color='white' if bright < .57 else '#1D2C3D')
    fig.text(.035,.965,'EXP-07 · Comparação de modelos',fontsize=10.25,weight='bold',color='#1D3449',va='top')
    fig.text(.035,.895,'F1 médio em cinco folds · validação por linhas',fontsize=7.9,color='#617080',va='top')
    fig.text(.035,.208,'A: 5 atributos    B: sem n_tx    C: 3 entropias',fontsize=7.65,color='#304454',va='center')
    fig.add_artist(plt.Line2D([.035,.96],[.165,.165],transform=fig.transFigure,color='#D9E1E7',lw=.8))
    fig.text(.035,.125,'Exploratório: 23 positivos de um único contrato.',fontsize=7.1,color='#9B542F',va='center')
    fig.text(.035,.075,'Não mede generalização para contratos inéditos.',fontsize=7.1,color='#526477',va='center')
    saida.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(saida,dpi=dpi,facecolor='white',bbox_inches='tight',pad_inches=.09)
    plt.close(fig)
    print('PNG:',saida.resolve())
    print('SHA-256 CSV:',checksum)
    print('F1 4×3:',mat)
    return checksum

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,default=Path('fig03_heatmap_coluna.png'))
    p.add_argument('--dpi',type=int,default=450)
    args=p.parse_args()
    gerar(args.input,args.output,args.dpi)
