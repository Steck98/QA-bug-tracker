from unittest.mock import patch

import pytest

from src.models.bug import Bug
from src.services.bug_manager import add_bug


@pytest.fixture
def bug_fixture():
    return Bug(
        title="Title",
        bug_id="BG-1234",
        status="DONE",
        priority="HIGH",
        description="asdasda",
        assigned_to="Raf",
        reported_by="Rafaa",
    )


def test_add_bug(bug_fixture):
    with patch("src.services.bug_manager.load_data") as mock_load_data:
        mock_load_data.return_value = {
            "users": [],
            "bugs": [],
        }
        with patch("src.services.bug_manager.add_data") as mock_add_data:
            add_bug(bug_fixture)
            mock_add_data.assert_called_once()


def test_existing_bug(bug_fixture):
    with patch("src.services.bug_manager.load_data") as mock_load_data:
        mock_load_data.return_value = {
            "users": [],
            "bugs": [
                {
                    "title": "Ttt",
                    "bug_id": "BG-1234",
                    "status": "TODO",
                    "priority": "HIGH",
                    "description": "ad",
                    "assigned_to": "Da",
                    "reported_by": "Da",
                },
                {
                    "title": "Ttt",
                    "bug_id": "BG-1234",
                    "status": "TODO",
                    "priority": "HIGH",
                    "description": "ad",
                    "assigned_to": "Da",
                    "reported_by": "Da",
                },
            ],
        }
        with patch("src.services.bug_manager.add_data") as mock_add_data:
            add_bug(bug_fixture)
            mock_add_data.assert_not_called()
