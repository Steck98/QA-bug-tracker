import json
import sys


def load_data(data_path="data/data.json"):
    try:
        with open(data_path, encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("FILE DOES NOT EXIST")
        sys.exit(1)
    except json.JSONDecodeError as error:
        print(
            f"JSON file corrupted at line {error.lineno}, column {error.colno}: {error.msg}"
        )
        sys.exit(1)


def add_data(new_data, data_path="data/data.json"):
    try:
        with open(data_path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {"users": [], "bugs": []}

    except json.JSONDecodeError as error:
        print(
            f"JSON file corrupted at line {error.lineno}, column {error.colno}: {error.msg}"
        )
        sys.exit(1)
    if "name" in new_data:
        data["users"].append(new_data)

    elif "title" in new_data:
        data["bugs"].append(new_data)
    try:
        with open(data_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except PermissionError:
        print("Permission denied: unable to write to data file.")
