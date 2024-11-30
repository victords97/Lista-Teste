import pytest
from revercao_string import reverter_string
def test_reverter_string():
    assert reverter_string("hello") == "olleh"
    assert reverter_string("abcd") == "dcba"
    assert reverter_string("") == ""