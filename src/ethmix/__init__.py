"""Funções de reprodução; implementação isolada e testável."""
from .features import FEATURES, DECIMAIS, preparar, entropia, calcular_features
from .models import novo_rf, reamostrar, validar_cv
