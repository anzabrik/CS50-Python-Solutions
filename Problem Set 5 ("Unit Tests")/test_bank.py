from bank import value


def test_hey():
    assert value("hey") == 20

def test_hello():
    assert value("hello") == 0

def test_yo():
    assert value("yo") == 100

def test_strip():
    assert value("  hey  ") == 20

def test_lower():
    assert value("HmM") == 20
