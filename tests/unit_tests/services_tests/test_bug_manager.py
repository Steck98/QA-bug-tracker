from unittest.mock import patch

import pytest

from src.models.bug import Bug
from src.services.bug_manager import (
    add_bug,
    choose_bug,
    delete_bug,
    display_bug,
    update_bug,
)


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


@pytest.fixture
def bug_data_fixture():
    return {
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
                "bug_id": "BG-1235",
                "status": "TODO",
                "priority": "HIGH",
                "description": "ad",
                "assigned_to": "Da",
                "reported_by": "Da",
            },
        ],
    }


@pytest.fixture
def empty_bug_data_fixture():
    return {
        "users": [],
        "bugs": [],
    }


def test_add_bug(bug_fixture, empty_bug_data_fixture):
    with patch("src.services.bug_manager.load_data") as mock_load_data:
        mock_load_data.return_value = empty_bug_data_fixture
        with patch("src.services.bug_manager.add_data") as mock_add_data:
            add_bug(bug_fixture)
            mock_add_data.assert_called_once()


def test_existing_bug(bug_fixture, bug_data_fixture):
    with patch("src.services.bug_manager.load_data") as mock_load_data:
        mock_load_data.return_value = bug_data_fixture
        with patch("src.services.bug_manager.add_data") as mock_add_data:
            add_bug(bug_fixture)
            mock_add_data.assert_not_called()


def test_choose_bug(bug_data_fixture):
    with patch("src.services.bug_manager.load_data") as mock_load_data:
        mock_load_data.return_value = bug_data_fixture
        with patch("src.services.bug_manager.input") as mock_input_data:
            mock_input_data.return_value = "1234"
            assert choose_bug("display")["bug_id"] == "BG-1234"


def test_choose_bug_retry(bug_data_fixture):
    with patch("src.services.bug_manager.load_data") as mock_load_data:
        mock_load_data.return_value = bug_data_fixture
        with patch("src.services.bug_manager.input") as mock_input_data:
            mock_input_data.side_effect = ["0001", "1235"]
            assert choose_bug("display")["bug_id"] == "BG-1235"


def test_display_bug(capsys):
    with patch("src.services.bug_manager.choose_bug") as mock_bug_data:
        mock_bug_data.return_value = {
            "title": "Ttt",
            "bug_id": "BG-1235",
            "status": "TODO",
            "priority": "HIGH",
            "description": "ad",
            "assigned_to": "Da",
            "reported_by": "Da",
        }
        display_bug()
        captured = capsys.readouterr()
        assert "ID: BG-1235" in captured.out


def test_delete_bug(bug_data_fixture):
    with patch("src.services.bug_manager.load_data") as mock_load_data:
        mock_load_data.return_value = bug_data_fixture
        with patch("src.services.bug_manager.choose_bug") as mock_single_bug_data:
            mock_single_bug_data.return_value = {
                "title": "Ttt",
                "bug_id": "BG-1235",
                "status": "TODO",
                "priority": "HIGH",
                "description": "ad",
                "assigned_to": "Da",
                "reported_by": "Da",
            }
            with patch("src.services.bug_manager.save_data") as mock_save_data:
                delete_bug()
                saved_data = mock_save_data.call_args[0][0]
                assert mock_single_bug_data.return_value not in saved_data["bugs"]


def test_update_bug(bug_data_fixture):
    with patch("src.services.bug_manager.load_data") as mock_load_data:
        mock_load_data.return_value = bug_data_fixture
        with patch("src.services.bug_manager.save_data") as mock_save_data:
            update_bug(
                {
                    "title": "Ttt",
                    "bug_id": "BG-1235",
                    "status": "TODO",
                    "priority": "HIGH",
                    "description": "ad",
                    "assigned_to": "Da",
                    "reported_by": "Da",
                },
                "title",
                "New Title",
            )
            saved_data = mock_save_data.call_args[0][0]
            assert any(
                x["title"] == "New Title" and x["bug_id"] == "BG-1235"
                for x in saved_data["bugs"]
            )
