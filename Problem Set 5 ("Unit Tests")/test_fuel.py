from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("2/4") == 50
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("4/2")
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ValueError):
        convert("1/2.5")
    with pytest.raises(ValueError):
        convert("cat/2.5")
    with pytest.raises(ValueError):
        convert("1-2")

    #assert convert("4/2") == 50



def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"

