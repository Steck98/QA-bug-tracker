import src.validators
from src.models.bug import Bug
from src.models.user import User
from src.services.bug_manager import (
    add_bug,
    choose_bug,
    delete_bug,
    display_bug,
    update_bug,
)
from src.services.employee_manager import (
    add_employee,
    choose_user,
    delete_user,
    display_user,
    update_user,
)


def run_bug_tracker():
    print("\n===============================")
    print("Welcome in  our Bug tracker App")
    print("===============================\n")
    while True:
        menu_choice = get_menu_choice()
        if menu_choice == 1:
            sub_menu_choice = get_sub_menu_choice("user")
            if sub_menu_choice == 1:
                get_user()
            if sub_menu_choice == 2:
                users_data_list = [
                    "last_name",
                    "position",
                    "employed",
                ]
                user = choose_user("update")
                while True:
                    print("last_name,position,employed")
                    user_field = input("Which field would you like to update").lower()
                    if src.validators.validate_choice(user_field, users_data_list):
                        while True:
                            if user_field == "position":
                                print("Change Position: JUNIORQA/QA/SENIORQA")
                                new_value = input("What is the new position? ").upper()
                                if src.validators.validate_choice(
                                    new_value, ["JUNIORQA", "QA", "SENIORQA"]
                                ):
                                    update_user(user, user_field, new_value)
                                    break
                            elif user_field == "employed":
                                print("Is employed?: yes/no")
                                new_value = input("What is the new status? ").lower()
                                if src.validators.validate_status(new_value):
                                    update_user(user, user_field, new_value)
                                    break
                            else:
                                new_value = get_text(
                                    "What is the new value?", True
                                ).lower()
                                update_user(user, user_field, new_value)
                                break
                    break
            if sub_menu_choice == 3:
                display_user()
            if sub_menu_choice == 4:
                delete_user()
        elif menu_choice == 2:
            sub_menu_choice = get_sub_menu_choice("bug")
            if sub_menu_choice == 1:
                get_bugs()
            if sub_menu_choice == 2:
                bugs_data_list = [
                    "title",
                    "status",
                    "priority",
                    "description",
                    "assigned_to",
                ]
                bug = choose_bug("update")
                while True:
                    print("Title,Status,Priority,Description,Assigned_to")
                    bug_field = input("Which field would you like to update").lower()
                    if src.validators.validate_choice(bug_field, bugs_data_list):
                        while True:
                            if bug_field == "priority":
                                print("Change Priority: LOW/MEDIUM/HIGH")
                                new_value = input("What is the new priority? ").upper()
                                if src.validators.validate_choice(
                                    new_value, ["LOW", "MEDIUM", "HIGH"]
                                ):
                                    update_bug(bug, bug_field, new_value)
                                    break
                            elif bug_field == "status":
                                print("Change Status: DONE/TODO/INPROGRESS")
                                new_value = input("What is the new status? ").upper()
                                if src.validators.validate_choice(
                                    new_value, ["TODO", "INPROGRESS", "DONE"]
                                ):
                                    update_bug(bug, bug_field, new_value)
                                    break
                            else:
                                new_value = get_text(
                                    "What is the new value?", True
                                ).lower()
                                update_bug(bug, bug_field, new_value)
                                break
                    break
            if sub_menu_choice == 3:
                display_bug()
            if sub_menu_choice == 4:
                delete_bug()
        else:
            break


def get_user():
    print("\n===============================")
    print("Add new user")
    print("===============================\n")
    return add_employee(
        User(
            name=get_text("Name: ", False),
            last_name=get_text("Last name: ", False),
            employee_id=get_id("Employee ID: ", "USR-"),
            employed=get_status(),
            position=get_choice("Position: ", User.allowed_positions),
        )
    )


def get_bugs():
    print("\n===============================")
    print("Submit bug report")
    print("===============================\n")
    return add_bug(
        Bug(
            title=get_text("Pick a title: ", True),
            bug_id=get_id("Bug ID: ", "BG-"),
            status=get_choice("What is the bug status? ", Bug.allowed_status),
            priority=get_choice("What is the bug priority? ", Bug.allowed_priorities),
            description=get_text("What is the issue? ", True),
            assigned_to=get_text("Who would you like to assign this bug to? ", False),
            reported_by=get_text("What is your name? ", False),
        )
    )


def get_menu_choice():
    while True:
        try:
            user_choice = int(
                input("Would you like to:\n1.Manage Users\n2.Manage Bugs\n3.Exit")
            )
            if 1 <= user_choice <= 3:
                return user_choice
            else:
                print("You must pick between 1 and 3")
        except ValueError:
            print("Your choice must consist of only digists")


def get_sub_menu_choice(category):
    print("\n===============================")
    print(f"Manage {category}")
    print("===============================\n")
    while True:
        try:
            user_choice = int(
                input(
                    f"Would you like to:\n1.Add {category}\n2.Update {category}\n3.Display {category}\n4.Delete {category}\n5.Return\n6.Exit"
                )
            )
            if 1 <= user_choice <= 6:
                return user_choice
            else:
                print("You must pick between 1 and 6")
        except ValueError:
            print("Your choice must consist of only digists")


def get_id(category, prefix):
    while True:
        new_id = input(category)
        validated_id = src.validators.validate_number(new_id)
        if validated_id:
            return f"{prefix}{new_id}"


def get_status():
    while True:
        status = input("Is employed? yes/no").lower()
        validated_status = src.validators.validate_status(status)
        if validated_status is not None:
            return validated_status


def get_text(default_text, special_text):
    while True:
        text = input(default_text)
        validated_text = src.validators.validate_text(text, special_text)
        if validated_text:
            return text


def get_choice(category, available_choices):
    while True:
        choice = input(category).upper()
        validated_choice = src.validators.validate_choice(choice, available_choices)
        if validated_choice:
            return choice
