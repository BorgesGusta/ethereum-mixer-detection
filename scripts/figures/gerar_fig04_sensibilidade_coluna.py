#!/usr/bin/env python3
"""Figura EXP-01J em UMA coluna, gerada dos dados oficiais com hash verificado.

Uso:
  python gerar_fig04_sensibilidade_coluna.py \
    --input comparacao_elegibilidade.csv \
    --output figuras/fig04_sensibilidade_coluna.png

Não estima precisão/recall e não rotula os alertas restantes.
"""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, FixedLocator
import pandas as pd

SHA256_ESPERADO='8c855262196d5fcadb92ddf9f4c8acc2c8de55b9262ebaf609ffec99623d9b87'
VALORES_ESPERADOS = {1:(230658,49,3), 5:(7865,14,3), 10:(4038,9,3), 20:(2464,7,3)}

def br(v): return f'{int(v):,}'.replace(',','.')

def gerar(entrada:Path, saida:Path, dpi:int=450):
    actual=hashlib.sha256(entrada.read_bytes()).hexdigest()
    if actual != SHA256_ESPERADO: raise ValueError('CSV não corresponde ao EXP-01J auditado: '+actual)
    d=pd.read_csv(entrada).sort_values('min_tx')
    if not {'min_tx','enderecos_unicos','alertas','pools_artigo_recuperados'}.issubset(d):
        raise ValueError('Colunas obrigatórias ausentes')
    got={int(r.min_tx):(int(r.enderecos_unicos),int(r.alertas),int(r.pools_artigo_recuperados)) for r in d.itertuples()}
    if got!=VALORES_ESPERADOS: raise ValueError('Valores fora da auditoria: '+str(got))
    x=d['min_tx'].to_numpy()
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8.2,
                         'axes.spines.top':False,'axes.spines.right':False})
    fig,(a,b)=plt.subplots(2,1,figsize=(3.55,4.05),facecolor='white')
    fig.subplots_adjust(left=.24,right=.95,top=.91,bottom=.115,hspace=.63)
    a.plot(x,d['enderecos_unicos'], '-o',linewidth=1.65,markersize=4.7)
    a.set_yscale('log'); a.set_ylim(1600,440000); a.set_xlim(.1,20.9)
    a.yaxis.set_major_locator(FixedLocator([2000,10000,100000]))
    a.yaxis.set_major_formatter(FuncFormatter(lambda v,pos: br(v)))
    a.minorticks_off(); a.grid(axis='y',alpha=.2,linewidth=.6)
    a.set_xticks([1,5,10,20],['1','5','10','20']); a.set_ylabel('Endereços elegíveis')
    a.set_title('(a) Cobertura · escala logarítmica',loc='left',fontsize=9.3,pad=8)
    for tx,val in zip(x,d['enderecos_unicos']):
        delta = (0,4) if tx not in (5,20) else (0,-12 if tx==5 else 5)
        a.annotate(br(val),(tx,val),xytext=delta,textcoords='offset points',ha='center',fontsize=8,weight='medium')
    b.plot(x,d['alertas'], '-o',linewidth=1.65,markersize=4.7)
    b.set_xlim(.1,20.9); b.set_ylim(0,59); b.set_yticks([0,20,40,60]);b.set_xticks([1,5,10,20])
    b.grid(axis='y',alpha=.2,linewidth=.6)
    b.set_title('(b) Contratos sinalizados',loc='left',fontsize=9.3,pad=8)
    b.set_ylabel('Alertas'); b.set_xlabel('Transações mínimas por endereço ($min_{tx}$)',labelpad=5)
    for tx,val in zip(x,d['alertas']):
        b.annotate(str(int(val)),(tx,val),xytext=(0,6),textcoords='offset points',ha='center',fontsize=8.4,weight='medium')
    # Legenda de escopo fica na legenda LaTeX, para não reduzir a legibilidade do gráfico.
    saida.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(saida,dpi=dpi,facecolor='white',bbox_inches='tight',pad_inches=.08)
    plt.close(fig)
    return actual

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,default=Path('fig04_sensibilidade_coluna.png'));p.add_argument('--dpi',type=int,default=450)
    args=p.parse_args();print('SHA-256 CSV:',gerar(args.input,args.output,args.dpi));print('PNG:',args.output)
