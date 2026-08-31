import pytest

from src.validators import validate_choice


@pytest.mark.parametrize(
    "choice,allowed_choices, expect",
    [
        (0, [1, 2, 3], False),
        (1, [1, 2, 3], True),
        (2, [1, 2, 3], True),
        (3, [1, 2, 3], True),
        (4, [1, 2, 3], False),
        ("asda", [1, 2, 3], False),
        ("", [1, 2, 3], False),
        ("   @#!  ", [1, 2, 3], False),
    ],
)
def test_validate_choice(choice, allowed_choices, expect):
    assert validate_choice(choice, allowed_choices) == expect
