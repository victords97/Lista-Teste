import pytest
from calculo_imposto import calcular_imposto
def test_calcular_imposto():
    assert calcular_imposto(2000) == 0
    assert calcular_imposto(3000) == 300
    assert calcular_imposto(6000) == 1200