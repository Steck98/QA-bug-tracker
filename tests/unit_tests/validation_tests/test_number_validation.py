import pytest

from src.validators import validate_number


@pytest.mark.parametrize(
    "number, expect",
    [
        ("123", False),
        ("1234", True),
        ("12345", False),
        ("asda ", False),
        ("12a31", False),
        ("0000", True),
    ],
)
def test_validate_number(number, expect):
    assert validate_number(number) == expect
