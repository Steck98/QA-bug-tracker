from models.bug import Bug
from models.user import User


def run_bug_tracker():
    print("\n===============================")
    print("Welcome in  our Bug tracker App")
    print("===============================\n")
    if get_choice() == 1:
        new_user = get_user()
        print(new_user)
    else:
        new_bug = bugs_inputs()
        print(new_bug)


def get_user():
    print("\n===============================")
    print("Add new user")
    print("===============================\n")
    return User(
        name=input("Name: "),
        last_name=input("Last name: "),
        employee_id=get_id("Employee ID: ", "USR-"),
        employed=get_status(),
        position=input("Position: "),
    )


def bugs_inputs():
    print("\n===============================")
    print("Submit bug report")
    print("===============================\n")
    return Bug(
        title=input("Pick a title: "),
        bug_id=get_id("Bug ID: ", "BG-"),
        status=input("What is the bug status? "),
        priority=input("What is the bug priority? "),
        description=input("What is the issue? "),
        assigned_to=input("Who would you like to assign this bug to? "),
        reported_by=input("What is your name? "),
    )


def get_choice():
    while True:
        try:
            user_choice = int(input("Would you like to:\n1.Add new user\n2.Report Bug"))
            print(user_choice)
            if 1 <= user_choice <= 2:
                return user_choice
            else:
                print("You must pick between 1 and 2")
        except ValueError:
            print("Your choice must consist of only digists")


def get_id(category, prefix):
    while True:
        try:
            return f"{prefix}{int(input(category))}"
        except ValueError:
            print("ID must consist of only numbers")


def get_status():
    while True:
        is_employed = input("Is employed? yes/no").lower()
        if is_employed == "yes":
            return True
        elif is_employed == "no":
            return False
        else:
            print("You must chose between yes/no")


run_bug_tracker()
