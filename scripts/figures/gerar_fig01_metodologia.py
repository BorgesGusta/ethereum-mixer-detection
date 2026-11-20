#!/usr/bin/env python3
"""Figura 1 (esquemática): fluxo metodológico dos EXP-01 a EXP-08.

Uso local/Colab:
    python gerar_fig01_metodologia.py --output fig01_metodologia.png

Nenhuma métrica ou resultado experimental é sintetizado nesta figura.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['pdf.fonttype'] = 42
rcParams['svg.fonttype'] = 'none'

NAVY = '#1E334A'
TEAL = '#0F827D'
DARK = '#263442'
GREY = '#68778A'
BORDER = '#DCE4EC'
LIGHT = '#F8FAFC'
BG = '#FFFFFF'
WARN = '#B66B31'


def build_figure(output: Path, dpi: int = 350) -> None:
    # A largura horizontal foi dimensionada para figure* (duas colunas do artigo).
    fig, ax = plt.subplots(figsize=(14, 3.6), dpi=180)
    fig.patch.set_facecolor(BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 3.6)
    ax.axis('off')
    fig.subplots_adjust(left=.018, right=.982, top=.98, bottom=.055)

    # Cabeçalho discreto: trabalho experimental e controle posterior.
    ax.text(.26, 3.34, 'PIPELINE DA PESQUISA', fontsize=10.2, weight='bold',
            color=NAVY, va='center', family='DejaVu Sans')
    ax.plot([.26, 9.05], [3.10, 3.10], color='#CBD6E2', lw=1.15)
    ax.text(9.30, 3.34, 'TRIAGEM E INTEGRIDADE', fontsize=10.2, weight='bold',
            color=TEAL, va='center')
    ax.plot([9.30, 13.75], [3.10, 3.10], color='#B8D6D2', lw=1.15)

    stages = [
        {'title':'Coleta', 'sub':'Dados da Ethereum', 'type':'research'},
        {'title':'Preparação', 'sub':'Filtros e agregação', 'type':'research'},
        {'title':'Atributos', 'sub':'5 variáveis (EXP-07)', 'type':'research'},
        {'title':'Modelagem', 'sub':'RF · DT · GB · RL', 'type':'research'},
        {'title':'Auditoria', 'sub':'Contratos e eventos', 'type':'defense'},
        {'title':'Triagem', 'sub':'Revisão + SHA-256', 'type':'defense'},
    ]
    left, w, sep, bottom, h = .18, 2.03, .29, 1.09, 1.77
    for i, stage in enumerate(stages):
        x = left + i*(w+sep)
        accent = NAVY if i < 4 else TEAL
        ax.add_patch(FancyBboxPatch((x, bottom), w, h,
                     boxstyle='round,pad=0.025,rounding_size=0.14',
                     linewidth=1.1, edgecolor=BORDER, facecolor=LIGHT))
        # Acento superior e marcador de etapa.
        ax.add_patch(FancyBboxPatch((x+.035, bottom+h-.085), w-.07, .055,
                     boxstyle='round,pad=0,rounding_size=.025',
                     linewidth=0, facecolor=accent))
        ax.add_patch(Circle((x+.25, bottom+h-.41), .165,
                            edgecolor='none', facecolor='#E2E9F1' if i < 4 else '#DDF0EB'))
        ax.text(x+.25, bottom+h-.41, str(i+1), ha='center', va='center',
                fontsize=11.1, fontweight='bold', color=accent)
        ax.text(x+.19, bottom+.77, stage['title'], ha='left', va='center',
                fontsize=14.1, color=DARK, fontweight='bold')
        ax.plot([x+.19, x+w-.20], [bottom+.56,bottom+.56],
                color='#E2E7ED', lw=1.0)
        ax.text(x+.19, bottom+.31, stage['sub'], ha='left', va='center',
                fontsize=10.6, color=GREY)

        if i < len(stages)-1:
            sx=x+w+.045
            ex=x+w+sep-.05
            arr=FancyArrowPatch((sx,bottom+.88),(ex,bottom+.88),
                                arrowstyle='-|>', mutation_scale=12,
                                color='#7891A4', lw=1.55)
            ax.add_patch(arr)

    # Conclusão metodológica: a previsão é um indicador sujeito à auditoria.
    ax.add_patch(FancyBboxPatch((2.45,.13),9.10,.55,
                 boxstyle='round,pad=.02,rounding_size=.12',
                 facecolor='#F3F7FA', edgecolor='#E1E9EE', linewidth=1))
    ax.add_patch(Circle((2.78,.405), .085, facecolor='#F8E9D8', edgecolor='none'))
    ax.text(2.78,.405,'!',ha='center',va='center',color=WARN,weight='bold',fontsize=11)
    ax.text(7.08,.405,'Alerta estatístico  ≠  identificação confirmada de um mixer',
            ha='center',va='center',color=DARK,fontsize=11.5,weight='medium')

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=dpi, facecolor='white', bbox_inches='tight', pad_inches=.16)
    plt.close(fig)
    print(f'Gerado: {output.resolve()}')


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--output', type=Path, default=Path('fig01_metodologia.png'))
    p.add_argument('--dpi', type=int, default=350)
    args=p.parse_args()
    build_figure(args.output, args.dpi)
