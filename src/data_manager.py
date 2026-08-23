import json


def display_data():
    with open("data/data.json", encoding="utf-8") as file:
        data = json.load(file)
        return data


def add_data(new_data):
    try:
        with open("data/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {"users": [], "bugs": []}

    except json.JSONDecodeError:
        data = {"users": [], "bugs": []}

    if "name" in new_data:
        data["users"].append(new_data)

    elif "title" in new_data:
        data["bugs"].append(new_data)

    with open("data/data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


test_data = [
    {
        "name": "Rafał",
        "last_name": "Stecz",
        "id": 1,
        "employed": True,
        "position": "QA Automation",
    },
    {
        "name": "Anna",
        "last_name": "Kowalska",
        "id": 2,
        "employed": True,
        "position": "Developer",
    },
    {
        "title": "Login button doesn't work",
        "id": "BUG-001",
        "status": "open",
        "priority": "high",
        "description": "Login button does nothing after clicking",
        "assigned_to": "Anna",
        "reported_by": "Rafał",
    },
    {
        "title": "Incorrect user data",
        "id": "BUG-002",
        "status": "in progress",
        "priority": "medium",
        "description": "User information is displayed incorrectly",
        "assigned_to": "Rafał",
        "reported_by": "Anna",
    },
]

for data in test_data:
    add_data(data)
