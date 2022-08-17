
import pytest

from main import discrim


testdata = [(1, 0, 0, 0), (1, 1, 0, 1), (1, 0, 1, -4), (1, 1, 1, -3), (0, 1, 1, 1), (1, -1, -2, 9)]


@pytest.mark.parametrize("a, b, c, d", testdata)
def test_discriminant(a, b, c, d):
    assert discrim(a, b, c) == d
