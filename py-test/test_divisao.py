import pytest
from divisao import dividir
def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(-10, 2) == -5
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)