import pytest
from ordenacao import ordenar
def test_ordenar():
    assert ordenar([3, 1, 2]) == [1, 2, 3]
    assert ordenar([10, -1, 3]) == [-1, 3, 10]
    assert ordenar([1]) == [1]