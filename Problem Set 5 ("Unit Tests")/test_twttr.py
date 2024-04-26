from twttr import shorten


def test_caps():
    assert shorten("AEIOUp") == "p"

def test_lowercase():
    assert shorten("paeiou") == "p"

def test_punctuation():
    assert shorten("p!@#$%^&*():;',.?-_~iou") == "p!@#$%^&*():;',.?-_~"

def test_numbers():
    assert shorten("p1234567890uio") == "p1234567890"
