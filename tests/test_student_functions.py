"""Pytest suite for the self‑assessment."""
import pytest
from src.student_functions import add, fibonacci, is_prime

# ----------------------------------------------------------------------
# add
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (2, 3, 5),
        (-4, 10, 6),
        (2.5, 0.5, 3.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected

# ----------------------------------------------------------------------
# fibonacci
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "n,expected",
    [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
    ],
)
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected

# ----------------------------------------------------------------------
# is_prime
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "n,expected",
    [
        (0, False),
        (1, False),
        (2, True),
        (17, True),
        (18, False),
    ],
)
def test_is_prime_basic(n, expected):
    assert is_prime(n) == expected


def test_is_prime_negative():
    with pytest.raises(ValueError):
        is_prime(-1)