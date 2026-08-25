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
