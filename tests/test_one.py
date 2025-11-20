import pytest

from problems.problem01 import get_42
from problems.problem02 import get_20


def test_get_42():
    assert get_42() == 42


def test_get_20():
    assert get_20() == 20
