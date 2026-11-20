#!/usr/bin/env python3
"""Figura 5 — arquitetura REAL do protótipo EXP-08, offline.

Reproduzir:
    pip install matplotlib
    python scripts/figures/gerar_fig05_triagem_exp08.py --output figures/fig05_triagem_exp08.png

É um DIAGRAMA de implementação (não uma medição, inferência on-chain ou
avaliação de eficácia de bloqueio). Reproduz o fluxo de triage.py:
  validate_case -> triage -> append_audit -> verify_audit.

Importante: receipt_ok/pool_log_verified são declarações fornecidas na entrada;
este protótipo NÃO verifica por RPC a veracidade dessas flags ou URLs.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

NAVY='#22344A'
TEAL='#168279'
INK='#24313F'
SOFT='#677789'
FRAME='#CFD9E2'
WHITE='#FFFFFF'
BACK='#F8FAFC'
MINT='#EDF7F5'


def make_figure(output: Path, dpi: int=350) -> None:
    plt.rcParams.update({'font.family':'DejaVu Sans','pdf.fonttype':42})
    fig, ax=plt.subplots(figsize=(12.2,3.85),facecolor=WHITE)
    ax.set(xlim=(0,12.2),ylim=(0,3.85))
    ax.axis('off')
    fig.subplots_adjust(left=.015,right=.985,bottom=.05,top=.96)

    ax.text(.20,3.55,'EXP-08  |  TRIAGEM DEFENSIVA DE ALERTAS',fontsize=13.2,fontweight='bold',color=NAVY,va='center')
    ax.plot([.20,12.0],[3.28,3.28],color=FRAME,lw=1.1)

    steps=[
      ('01','Entrada do caso',['Contrato + score','Evidências fornecidas'],'input'),
      ('02','Validação',['Formato de endereço','Hash e URL declarada'],'format'),
      ('03','Priorização',['Coletar ou revisar','evidências informadas'],'flow'),
      ('04','Registro auditável',['JSONL + SHA-256','Verificação de integridade'],'audit'),
    ]
    xs=[.22,3.30,6.38,9.46]
    w=2.53; y=1.24; h=1.72
    for i,(num,name,desc,kind) in enumerate(steps):
        x=xs[i]
        accent=NAVY if i<2 else TEAL
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.025,rounding_size=.125',facecolor=BACK if i<2 else MINT,edgecolor=FRAME,linewidth=1.25))
        ax.add_patch(Circle((x+.38,y+h-.35),.18,facecolor='#E4EAF0' if i<2 else '#D7ECE7',edgecolor='none'))
        ax.text(x+.38,y+h-.35,num,ha='center',va='center',fontsize=10.0,fontweight='bold',color=accent)
        ax.text(x+.20,y+.89,name,fontsize=12.8,fontweight='bold',color=INK,va='center')
        ax.plot([x+.20,x+w-.20],[y+.71,y+.71],color=FRAME,lw=.75)
        ax.text(x+.20,y+.47,desc[0],fontsize=9.95,color=SOFT,va='center')
        ax.text(x+.20,y+.21,desc[1],fontsize=9.95,color=SOFT,va='center')
        if i<3:
            a=FancyArrowPatch((x+w+.075,y+.87),(xs[i+1]-.11,y+.87),arrowstyle='-|>',mutation_scale=14,linewidth=1.5,color='#728A9B')
            ax.add_patch(a)

    # The implemented prototype returns 'indeterminado' for *all* cases:
    ax.text(.25,.99,'Saída atual:',fontsize=10.2,fontweight='bold',color=NAVY,va='center')
    ax.text(1.42,.99,'indeterminado  •  revisão humana necessária  •  sem bloqueio automático',fontsize=10.4,color=TEAL,va='center')
    ax.add_patch(FancyBboxPatch((.20,.16),11.82,.47,boxstyle='round,pad=.025,rounding_size=.075',facecolor='#F0F4F7',edgecolor='#E1E7ED',linewidth=.7))
    ax.text(6.11,.405,'Protótipo offline: flags e URLs são informadas pelo operador; não há consulta RPC, SIEM nem verificação externa.',fontsize=9.35,color=SOFT,ha='center',va='center')

    output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,dpi=dpi,bbox_inches='tight',pad_inches=.14,facecolor='white')
    plt.close(fig)
    print(f'Gerado: {output.resolve()}')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,default=Path('fig05_triagem_exp08.png'))
    p.add_argument('--dpi',type=int,default=350)
    args=p.parse_args()
    make_figure(args.output,args.dpi)
