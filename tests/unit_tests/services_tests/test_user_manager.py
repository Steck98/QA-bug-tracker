from unittest.mock import patch

import pytest

from src.models.user import User
from src.services.employee_manager import (
    add_employee,
    choose_user,
    delete_user,
    display_user,
    update_user,
)


@pytest.fixture
def employee_fixture():
    return User(
        name="Raf",
        last_name="Das",
        employee_id="USR-1234",
        employed=False,
        position="QA",
    )


@pytest.fixture
def user_data_fixture():
    return {
        "users": [
            {
                "name": "Jan",
                "last_name": "Kowalski",
                "employee_id": "USR-1234",
                "employed": True,
                "position": "QA",
            },
            {
                "name": "Raf",
                "last_name": "Kaczkowski",
                "employee_id": "USR-1235",
                "employed": False,
                "position": "QA",
            },
        ],
        "bugs": [],
    }


def test_add_new_employee(employee_fixture):

    with patch("src.services.employee_manager.load_data") as mock_load_data:
        mock_load_data.return_value = {
            "users": [],
            "bugs": [],
        }

        with patch("src.services.employee_manager.add_data") as mock_add_data:
            add_employee(employee_fixture)

            mock_load_data.assert_called()
            mock_add_data.assert_called_once()


def test_existing_employee(employee_fixture, user_data_fixture):
    with patch("src.services.employee_manager.load_data") as mock_load_data:
        mock_load_data.return_value = user_data_fixture

        with patch("src.services.employee_manager.add_data") as mock_add_data:
            add_employee(employee_fixture)
            mock_load_data.assert_called()
            mock_add_data.assert_not_called()


def test_choose_user(user_data_fixture):
    with patch("src.services.employee_manager.load_data") as mock_load_data:
        mock_load_data.return_value = user_data_fixture
        with patch("src.services.employee_manager.input") as mock_input_data:
            mock_input_data.return_value = "1234"
            assert choose_user("display")["employee_id"] == "USR-1234"


def test_choose_user_retry(user_data_fixture):
    with patch("src.services.employee_manager.load_data") as mock_load_data:
        mock_load_data.return_value = user_data_fixture
        with patch("src.services.employee_manager.input") as mock_input_data:
            mock_input_data.side_effect = ["0001", "1234"]
            assert choose_user("display")["employee_id"] == "USR-1234"


def test_display_user(capsys, user_data_fixture):
    with patch("src.services.employee_manager.choose_user") as mock_user_data:
        mock_user_data.return_value = user_data_fixture["users"][0]
        display_user()
        captured = capsys.readouterr()
        assert "ID: USR-1234" in captured.out


def test_delete_user(user_data_fixture):
    with patch("src.services.employee_manager.load_data") as mock_load_data:
        mock_load_data.return_value = user_data_fixture
        with patch(
            "src.services.employee_manager.choose_user"
        ) as mock_single_user_data:
            mock_single_user_data.return_value = user_data_fixture["users"][0]
            with patch("src.services.employee_manager.save_data") as mock_save_data:
                delete_user()
                saved_data = mock_save_data.call_args[0][0]
                assert mock_single_user_data.return_value not in saved_data["users"]


def test_update_user(user_data_fixture):
    with patch("src.services.employee_manager.load_data") as mock_load_data:
        mock_load_data.return_value = user_data_fixture
        with patch("src.services.employee_manager.save_data") as mock_save_data:
            update_user(
                user_data_fixture["users"][0],
                "name",
                "Tom",
            )
            saved_data = mock_save_data.call_args[0][0]
            assert any(
                x["name"] == "Tom" and x["employee_id"] == "USR-1234"
                for x in saved_data["users"]
            )
