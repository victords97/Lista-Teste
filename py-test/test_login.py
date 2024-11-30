import pytest
from login import logar
def test_login():
    assert logar("admin", "1234") == True
    assert logar("usuario", "senha123") == True
    assert logar("admin", "senhaerrada") == False
    assert logar("invalido", "senha123") == False