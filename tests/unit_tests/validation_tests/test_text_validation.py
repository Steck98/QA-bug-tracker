import pytest

from src.validators import validate_text


@pytest.mark.parametrize(
    "text,expect",
    [
        (("a" * 1), False),
        (("a" * 2), True),
        (("a" * 3), True),
        (("     "), False),
        (("!@#!#!"), False),
        (("2someString"), False),
        (("    Rafał    "), True),
        (("rafał   "), True),
    ],
)
def test_validate_text(text, expect):
    assert validate_text(text) == expect


@pytest.mark.parametrize(
    "spec_text,expect",
    [
        (("a" * 5), False),
        (("a" * 6), True),
        (("a" * 7), True),
        (("a" * 100), True),
        (("a" * 499), True),
        (("a" * 500), True),
        (("a" * 501), False),
    ],
)
def test_special_text(spec_text, expect):
    assert validate_text(spec_text, special_text=True) == expect
