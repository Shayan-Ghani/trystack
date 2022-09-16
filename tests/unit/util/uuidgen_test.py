import pytest

from trystack.util import uuidgen

def test_uuidgen():
    result = uuidgen()
    assert type(result) is str
    assert len(result) == 32 
    assert result.isalnum() is True

