import pytest
from numerando import numerar
def test_numerar():
    numero = numerar(1, 10)
    assert 1 <= numero <= 10