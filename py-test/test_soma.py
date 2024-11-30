import pytest
from soma import somar
# Testa a função soma
def test_soma():
    assert somar(1, 2, 3) == 6
    assert somar(-1, -2, -3) == -6
    assert somar(0, 0, 0) == 0

