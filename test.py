
import pytest

from main import discrim, main

testdata = [(1, 0, 0, 0), (1, 1, 0, 1), (1, 0, 1, -4), (1, 1, 1, -3), (0, 1, 1, 1), (1, -1, -2, 9)]


@pytest.mark.parametrize("a, b, c, d", testdata)
def test_discriminant(a, b, c, d):
    assert discrim(a, b, c) == d


def test_main_1():
    assert main(0, 1, 1) == 'division by zero'

def test_main_2(d='ff'):
    assert main(d, 1, 1) == "could not convert string to float"

def test_main_3():
    assert main(1, 0, 1) == "negative discriminant"

def test_main_4():
    assert main(True, 0, 1) == "negative discriminant"