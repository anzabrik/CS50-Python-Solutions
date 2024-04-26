import pytest
from numb3rs import validate


def main():
    test_validate_in()
    test_validate_punc()
    test_validate_structure()
    test_check()


def test_validate_in():
    assert validate("12.12.12.12") == True
    assert validate("0.12.12.12") == True
    assert validate("255.255.255.255") == True
    assert validate("256.12.12.12") == False
    assert validate("-1.12.12.12") == False
    assert validate(".12.12.12") == False
    assert validate("12.777.12.12") == False
    assert validate("12.12.777.12") == False
    assert validate("12.12.12.777") == False
    assert validate("12.12.12.cat") == False


def test_validate_punc():
    assert validate("12,12.12.12") == False
    assert validate("12.12/12.12") == False


def test_validate_structure():
    assert validate("12.12.12.12.12") == False
    assert validate("12.12.12") == False


if __name__ == "__main__":
    main()
