import unittest
import numpy as np
import pandas as pd
from ethmix.features import calcular_features, preparar, FEATURES
from ethmix.models import novo_rf, reamostrar, validar_cv

class TestFeatures(unittest.TestCase):
    def setUp(self):
        self.tx=pd.DataFrame({
            "hash":["a","b","c","d","e","f"],
            "time":["2020-10-29T01:00:00Z"]*6,
            "recipient":["0xAb","0xAb","0xAb","0xCd","0xCd","0xCd"],
            "sender":["0x1"]*6,
            "call_count":[2,4,6,10,10,10],
            "value_eth":[1.,1.,2.,3.,3.,3.],
            "fee_eth":[.01,.01,.02,.03,.03,.03],
            "internal_value_eth":[1.,1.,1.,2.,2.,2.]})
    def test_preparar_normalizacao(self):
        raw=preparar(self.tx)
        self.assertEqual(set(raw.recipient),{"0xab","0xcd"})
        self.assertEqual(str(raw.dia.iloc[0]),"2020-10-29")
    def test_entropia_e_constancia(self):
        fs=calcular_features(preparar(self.tx)).set_index("recipient")
        self.assertEqual(len(fs),2)
        self.assertEqual(int(fs.loc["0xab","n_tx"]),3)
        self.assertAlmostEqual(fs.loc["0xab","value_entropy"],0.9182958340544896,places=10)
        self.assertAlmostEqual(fs.loc["0xab","internal_value_entropy"],0.,places=12)
        self.assertAlmostEqual(fs.loc["0xab","call_count_mean"],4.)
        self.assertAlmostEqual(fs.loc["0xcd","value_entropy"],0.,places=12)
    def test_wei(self):
        df=self.tx.drop(columns=["value_eth","fee_eth","internal_value_eth"])
        df["value"]=[1e18,1e18,2e18,3e18,3e18,3e18]
        df["fee"]=[1e16,1e16,2e16,3e16,3e16,3e16]
        df["internal_value"]=[1e18,1e18,1e18,2e18,2e18,2e18]
        self.assertAlmostEqual(preparar(df).value_eth.iloc[2],2.)
    def test_oversampling(self):
        X=pd.DataFrame({f:np.arange(8,dtype=float) for f in FEATURES})
        y=pd.Series([1]+[0]*7)
        a,b=reamostrar(X,y,42)
        self.assertEqual(b.value_counts().to_dict(),{0:7,1:7})
        self.assertEqual(len(a),14)
    def test_modelo(self):
        model=novo_rf()
        self.assertEqual(model.n_estimators,100)
        self.assertEqual(model.max_depth,5)

if __name__=="__main__":
    unittest.main()
