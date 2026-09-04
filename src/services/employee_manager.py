from src.services.data_manager import add_data, load_data, save_data
from src.validators import validate_number


def add_employee(new_employee):
    if load_data() != None:
        employee_id_list = [
            employee["employee_id"] for employee in load_data()["users"]
        ]
        if not new_employee.employee_id in employee_id_list:
            add_data(new_employee.to_dict())
        else:
            print("employee with this ID is arleady in our system")


def choose_user(action):
    while True:
        users_data = load_data()["users"]
        print("\n===============================")
        print("Active users:")
        print("===============================")
        for user in users_data:
            print(f"{user['name']} {user['last_name']}:")
            print(f"{user['employee_id']}\n")
        picked_user = input(f"Which user would you like to {action}? Pick by ID digits")
        if validate_number(picked_user):
            for user in users_data:
                if f"USR-{picked_user}" == user["employee_id"]:
                    return user
                else:
                    print("Picked user does not exist, pick one from the list")


def display_user():
    user = choose_user("display")
    print("\n===============================")
    print(f"Name: {user['name']}")
    print(f"Last Name: {user['last_name']}")
    print(f"ID: {user['employee_id']}")
    print(f"Is employed: {user['employed']}")
    print(f"Position: {user['position']}")
    print("\n===============================")


def delete_user():
    users_data = load_data()
    user = choose_user("delete")
    users_data["users"].remove(user)
    save_data(users_data)


def update_user(single_user, user_field, new_value):
    data = load_data()
    for user in data["users"]:
        if single_user["employee_id"] == user["employee_id"]:
            user[user_field] = new_value
    save_data(data)
