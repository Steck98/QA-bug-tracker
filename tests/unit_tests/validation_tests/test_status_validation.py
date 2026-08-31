import pytest

from src.validators import validate_status


@pytest.mark.parametrize(
    "status, expect",
    [
        ("yes", True),
        ("no", False),
        ("Yes", None),
        ("12345", None),
        ("asda ", None),
        ("12a31", None),
        ("0000", None),
        ("   @#@", None),
        ("   yes   ", None),
    ],
)
def test_validate_status(status, expect):
    assert validate_status(status) == expect
