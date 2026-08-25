import validators
from models.bug import Bug
from models.user import User
from services.bug_manager import add_bug
from services.employee_manager import add_employee


def run_bug_tracker():
    print("\n===============================")
    print("Welcome in  our Bug tracker App")
    print("===============================\n")
    while True:
        menu_choice = get_menu_choice()
        if menu_choice == 1:
            get_user()
        elif menu_choice == 2:
            bugs_inputs()
        else:
            break


def get_user():
    print("\n===============================")
    print("Add new user")
    print("===============================\n")
    return add_employee(
        User(
            name=get_text("Name: "),
            last_name=get_text("Last name: "),
            employee_id=get_id("Employee ID: ", "USR-"),
            employed=get_status(),
            position=get_choice("Position: ", User.allowed_positions),
        )
    )


def bugs_inputs():
    print("\n===============================")
    print("Submit bug report")
    print("===============================\n")
    return add_bug(
        Bug(
            title=input("Pick a title: "),
            bug_id=get_id("Bug ID: ", "BG-"),
            status=get_choice("What is the bug status? ", Bug.allowed_status),
            priority=get_choice("What is the bug priority? ", Bug.allowed_priorities),
            description=input("What is the issue? "),
            assigned_to=get_text("Who would you like to assign this bug to? "),
            reported_by=get_text("What is your name? "),
        )
    )


def get_menu_choice():
    while True:
        try:
            user_choice = int(
                input("Would you like to:\n1.Add new user\n2.Report Bug\n3.Exit")
            )
            if 1 <= user_choice <= 3:
                return user_choice
            else:
                print("You must pick between 1 and 3")
        except ValueError:
            print("Your choice must consist of only digists")


def get_id(category, prefix):
    while True:
        new_id = input(category)
        validated_id = validators.validate_number(new_id)
        if validated_id:
            return f"{prefix}{new_id}"


def get_status():
    while True:
        status = input("Is employed? yes/no").lower()
        validated_status = validators.validate_status(status)
        if validated_status is not None:
            return validated_status


def get_text(default_text):
    while True:
        text = input(default_text)
        validated_text = validators.validate_text(text)
        if validated_text:
            return text.capitalize()


def get_choice(category, available_choices):
    while True:
        choice = input(category).upper()
        validated_choice = validators.validate_choice(choice, available_choices)
        if validated_choice:
            return choice
