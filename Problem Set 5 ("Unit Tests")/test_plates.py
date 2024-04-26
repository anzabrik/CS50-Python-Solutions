from plates import is_valid

def test_two_letters():
    assert is_valid("1bb") == False
    assert is_valid("11b") == False
    assert is_valid("bbb") == True
    assert is_valid("123") == False

def test_char_count():
    assert is_valid("abab121") == False
    assert is_valid("abab121") == False
    assert is_valid("abab12") == True
    assert is_valid("aba1") == True

def test_no_numbers_middle():
    assert is_valid("at1a") == False

def test_zero():
    assert is_valid("ab0") == False

def test_punctuation():
    assert is_valid("ab,:1") == False
