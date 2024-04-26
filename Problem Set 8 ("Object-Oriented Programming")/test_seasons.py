from seasons import get_age
import pytest

def main():
    test_format()
    test_values()



def test_format():
    with pytest.raises(SystemExit) as sample:
        get_age("1812-05-05")
    assert sample.type == SystemExit

    with pytest.raises(SystemExit) as sample:
        get_age("5 February 1987")
    assert sample.type == SystemExit



def test_values():
    assert get_age("1991-01-01") == "Seventeen million, sixteen thousand, four hundred eighty minutes"
    assert get_age("2001-01-01") == "Eleven million, seven hundred fifty-six thousand, one hundred sixty minutes"


if __name__ == "__main__":
    main()


