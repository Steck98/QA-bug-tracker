from unittest.mock import patch

import pytest

from src.models.user import User
from src.services.employee_manager import add_employee


@pytest.fixture
def employee_fixture():

    return User(
        name="Raf",
        last_name="Das",
        employee_id="USR-1234",
        employed=False,
        position="QA",
    )


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


def test_existing_employee(employee_fixture):

    with patch("src.services.employee_manager.load_data") as mock_load_data:
        mock_load_data.return_value = {
            "users": [
                {
                    "name": "Jan",
                    "last_name": "Kowalski",
                    "employee_id": "USR-1234",
                    "employed": True,
                    "position": "QA",
                }
            ],
            "bugs": [],
        }

        with patch("src.services.employee_manager.add_data") as mock_add_data:
            add_employee(employee_fixture)

            mock_load_data.assert_called()
            mock_add_data.assert_not_called()
