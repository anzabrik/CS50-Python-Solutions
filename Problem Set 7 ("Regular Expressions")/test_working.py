from working import convert
import pytest

def main():
    test_convert_format()
    test_convert_hours()
    test_convert_minutes()

# Check whether

def test_convert_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM : 5 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")


def test_convert_minutes():
    assert convert("9:30 AM to 5:00 PM") == "09:30 to 17:00"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")


def test_convert_hours():
    assert convert("12:00 AM to 5:00 PM") == "00:00 to 17:00"
    assert convert("12 AM to 5 PM") == "00:00 to 17:00"
    assert convert("9:00 AM to 12:00 PM") == "09:00 to 12:00"
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 14:00 PM")


if __name__ == "__main__":
    main()