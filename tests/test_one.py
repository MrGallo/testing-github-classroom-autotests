import pytest

def test_add():
    assert 2 + 2 == 4

def test_subtract():
    assert 5 - 3 == 2

def test_multiply():
    assert 3 * 4 == 12

def test_divide():
    assert 10 / 2 == 5

def test_string_upper():
    assert "hello".upper() == "HELLO"
