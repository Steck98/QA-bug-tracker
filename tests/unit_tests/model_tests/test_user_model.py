import pytest

from src.models.user import User

# ==================================================
# KONSTRUKTOR
# ==================================================


@pytest.mark.parametrize(
    "name, last_name, employee_id, employed, position",
    [
        ("Rafał", "Stecz", "1312", True, "JUNIORQA"),
        ("Rafałaa", "Stecza", "13123", False, "JUNIORQA"),
    ],
)
def test_user_class(name, last_name, employee_id, employed, position):
    user = User(
        name=name,
        last_name=last_name,
        employee_id=employee_id,
        employed=employed,
        position=position,
    )
    assert user.employee_id == employee_id
    assert user.position == position
    assert user.employed == employed
    assert user.last_name == last_name
    assert user.to_dict()["name"] == name


# ==================================================
# GETTERY
# ==================================================


@pytest.fixture
def user_fixture():
    return User(
        name="Rafał",
        last_name="Stecz",
        employee_id="1234",
        employed=True,
        position="JUNIORQA",
    )


def test_get_user_id(user_fixture):
    assert user_fixture.employee_id == "1234"


def test_get_user_position(user_fixture):
    assert user_fixture.position == "JUNIORQA"


def test_get_user_employed(user_fixture):
    assert user_fixture.employed == True


def test_get_user_last_name(user_fixture):
    assert user_fixture.last_name == "Stecz"


# ==================================================
# SETTERY
# ==================================================


@pytest.mark.parametrize(
    "user_last_name", ["Kowalski", "jabłkowicz", "lewandowski", "TinkiWinki"]
)
def test_set_user_last_name(user_fixture, user_last_name):
    user_fixture.last_name = user_last_name
    assert user_fixture.last_name == user_last_name


@pytest.mark.parametrize("user_position", ["QA", "JUNIORQA"])
def test_set_user_position(user_fixture, user_position):
    user_fixture.position = user_position
    assert user_fixture.position == user_position


@pytest.mark.parametrize("user_employed", [True, False])
def test_set_user_employed(user_fixture, user_employed):
    user_fixture.employed = user_employed
    assert user_fixture.employed == user_employed


# ==================================================
# TO DICT
# ==================================================


def test_user_to_dict(user_fixture):
    user_dict = user_fixture.to_dict()
    assert user_dict == {
        "name": "Rafał",
        "last_name": "Stecz",
        "employee_id": "1234",
        "employed": True,
        "position": "JUNIORQA",
    }


# ==================================================
# REPR
# ==================================================


def test_user_repr(user_fixture):
    assert repr(user_fixture) == (
        f"Name: Rafał\nLast name: {user_fixture.last_name}\nid: {user_fixture.employee_id}\nemployed: {user_fixture.employed}\nposition: {user_fixture.position}"
    )
