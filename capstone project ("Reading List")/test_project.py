import pytest
from project import search_author, remove_book, add_book


def test_search_author():
    assert search_author("Vladimir Nabokov") == True
    assert search_author("vladimir nabokov") == True
    assert search_author("Puskin Alex") == False


def test_add_book():
    assert add_book("Pale Fire") == True
    assert add_book("pale fire") == True
    assert add_book("Birght Light") == False


def test_remove_book():
    assert remove_book("Pale Fire") == True
    assert remove_book("pale fire") == True
    assert remove_book("Birght Light") == False
