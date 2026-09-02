from unittest.mock import patch

from src.input_handler import get_choice, get_id, get_menu_choice, get_status, get_text


def test_menu_choice():
    with patch("src.input_handler.input") as mock_user_choice:
        mock_user_choice.return_value = "1"
        assert get_menu_choice() == 1


def test_wrong_value_menu_choice():
    with patch("src.input_handler.input") as mock_user_choice:
        mock_user_choice.side_effect = ["abc", "2"]
        assert get_menu_choice() == 2


def test_get_id():
    with patch("src.input_handler.input") as mock_get_id:
        mock_get_id.return_value = "1234"
        assert get_id("", "USR-") == "USR-1234"


def test_get_id_retry():
    with patch("src.input_handler.input") as mock_get_id:
        mock_get_id.side_effect = ["123", "2231"]
        assert get_id("", "USR-") == "USR-2231"


def test_get_status():
    with patch("src.input_handler.input") as mock_get_status:
        mock_get_status.return_value = "yes"
        assert get_status() is True


def test_get_status_retry():
    with patch("src.input_handler.input") as mock_get_status:
        mock_get_status.side_effect = ["Fake test", "no"]
        assert get_status() is False


def test_get_text():
    with patch("src.input_handler.input") as mock_get_text:
        mock_get_text.return_value = "This is my testing text!!!!! where 1 2 3 4 is allowed and all kind of Łeird signs"
        assert (
            get_text("", True)
            == "This is my testing text!!!!! where 1 2 3 4 is allowed and all kind of Łeird signs"
        )


def test_get_restricted_text():
    with patch("src.input_handler.input") as mock_get_text:
        mock_get_text.return_value = "ThisTestIsRestriktedToOnlyLetters"
        assert get_text("", False) == "ThisTestIsRestriktedToOnlyLetters"


def test_get_text_retry():
    with patch("src.input_handler.input") as mock_get_text:
        mock_get_text.side_effect = [" ", "Retry after a wrong input string :D "]
        assert get_text(" ", True) == "Retry after a wrong input string :D "


def test_get_restricted_text_retry():
    with patch("src.input_handler.input") as mock_get_text:
        mock_get_text.side_effect = ["This is a restricted text test :D ", "Working"]
        assert get_text(" ", False) == "Working"


def test_get_choice():
    with patch("src.input_handler.input") as mock_get_choice:
        mock_get_choice.return_value = "Todo"
        assert get_choice("", ["TODO", "INPROGRESS", "DONE"]) == "TODO"


def test_get_choice_retry():
    with patch("src.input_handler.input") as mock_get_choice:
        mock_get_choice.side_effect = ["CEO", "DONE"]
        assert get_choice("", ["TODO", "INPROGRESS", "DONE"]) == "DONE"
