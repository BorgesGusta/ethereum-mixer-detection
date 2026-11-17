"""Modelo de reprodução legado; não substitui modelo salvo no Drive."""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import resample
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
from .features import FEATURES

def novo_rf(seed=42):
    return RandomForestClassifier(
        n_estimators=100,max_depth=5,class_weight="balanced",random_state=seed)

def reamostrar(X:pd.DataFrame,y:pd.Series,seed=42):
    """Oversampling só sobre dados de treino. Preserva a semântica legada."""
    d=X.copy().assign(_y=np.asarray(y))
    maj,mino=d[d._y==0],d[d._y==1]
    if not len(maj) or not len(mino):
        raise ValueError("É necessário ter as duas classes.")
    if len(mino)<len(maj):
        mino=resample(mino,replace=True,n_samples=len(maj),random_state=seed)
    balanced=pd.concat([maj,mino])
    return balanced[list(X.columns)],balanced["_y"].astype(int)

def validar_cv(df:pd.DataFrame,seed=42,n_splits=5):
    X,y=df[list(FEATURES)],df["label"].astype(int)
    if y.value_counts().min()<n_splits:
        raise ValueError("Poucos exemplos para o número solicitado de folds.")
    skf=StratifiedKFold(n_splits=n_splits,shuffle=True,random_state=seed)
    rows=[]
    for fold,(itr,iva) in enumerate(skf.split(X,y),1):
        Xt,yt=reamostrar(X.iloc[itr],y.iloc[itr],seed)
        model=novo_rf(seed).fit(Xt,yt)
        pred=model.predict(X.iloc[iva])
        tn,fp,fn,tp=confusion_matrix(y.iloc[iva],pred,labels=[0,1]).ravel()
        rows.append({"fold":fold,"precision":precision_score(y.iloc[iva],pred,zero_division=0),
          "recall":recall_score(y.iloc[iva],pred,zero_division=0),
          "f1":f1_score(y.iloc[iva],pred,zero_division=0),
          "tp":int(tp),"fp":int(fp),"fn":int(fn),"tn":int(tn)})
    return pd.DataFrame(rows)
