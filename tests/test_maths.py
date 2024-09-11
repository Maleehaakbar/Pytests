import math
import pytest

def test_sqrt():
    num=25
    assert math.sqrt(num)==5
def test_square():
    num=7
    assert 7*7 ==45
def test_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):  #context manager
        1/0


