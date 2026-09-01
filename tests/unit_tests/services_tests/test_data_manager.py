from unittest.mock import patch

import pytest

from src.services.data_manager import *


@pytest.fixture
def temp_json_file(tmp_path):
    return tmp_path / "data.json"


@pytest.fixture
def corrupted_json_file(tmp_path):
    corrupted_file = tmp_path / "data_cor.json"
    corrupted_file.write_text('{"name": "Rafal"')
    return corrupted_file


@pytest.fixture
def non_existing_json_file(tmp_path):
    return tmp_path / "data_empty.json"


# ==================================================
# LOAD DATA
# ==================================================


def test_load_empty_manager(non_existing_json_file):
    with pytest.raises(SystemExit):
        load_data(non_existing_json_file)


def test_load_corrupted_json_data_manager(corrupted_json_file):
    with pytest.raises(SystemExit):
        load_data(corrupted_json_file)


# ==================================================
# ADD DATA
# ==================================================


@pytest.mark.parametrize(
    "user_data",
    [
        {
            "name": "Raf",
            "last_name": "Dsa",
            "employee_id": "USR-3123",
            "employed": False,
            "position": "QA",
        },
        {
            "name": "Raf",
            "last_name": "Das",
            "employee_id": "USR-1942",
            "employed": False,
            "position": "QA",
        },
    ],
)
def test_add_user_data(user_data, temp_json_file):
    add_data(user_data, temp_json_file)
    saved_data = load_data(temp_json_file)
    assert user_data in saved_data["users"]


@pytest.mark.parametrize(
    "bug_data",
    [
        {
            "title": "Title",
            "bug_id": "BG-1234",
            "status": "DONE",
            "priority": "HIGH",
            "description": "asdasda",
            "assigned_to": "Raf",
            "reported_by": "Rafaa",
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
)
def test_add_bug_data(bug_data, temp_json_file):
    add_data(bug_data, temp_json_file)
    saved_data = load_data(temp_json_file)
    assert bug_data in saved_data["bugs"]


@pytest.mark.parametrize(
    "bug_data",
    [
        {
            "title": "Title",
            "bug_id": "BG-1234",
            "status": "DONE",
            "priority": "HIGH",
            "description": "asdasda",
            "assigned_to": "Raf",
            "reported_by": "Rafaa",
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
)
def test_add_corrupted_json_data_manager(bug_data, corrupted_json_file):
    with pytest.raises(SystemExit):
        add_data(bug_data, corrupted_json_file)


def test_permission_error_data_manager(temp_json_file):
    bug_data = {
        "title": "Test bug",
        "bug_id": "BG-1234",
        "status": "TODO",
        "priority": "HIGH",
        "description": "Test",
        "assigned_to": "Raf",
        "reported_by": "Raf",
    }
    original_open = open

    def open_side_effect(file, mode="r", *args, **kwargs):
        if mode == "w":
            raise PermissionError()
        return original_open(file, mode, *args, **kwargs)

    with patch("src.services.data_manager.open", side_effect=open_side_effect):
        add_data(bug_data, temp_json_file)
