from um import count

def main():
    test_count()
    test_count()
    test_count()


def test_count_punc():
    assert count("um") == 1
    assert count("um?") == 1
    assert count(", um, ") == 1
    assert count(", um, um, um") == 3


def test_count_words():
    assert count("mum") == 0
    assert count("umm") == 0
    assert count("brum") == 0
    assert count("brum, um, dum") == 1


def test_count_case():
    assert count("Um") == 1
    assert count(", Um, ") == 1
    assert count(", um, um, Um") == 3


if __name__ == "__main__":
    main()