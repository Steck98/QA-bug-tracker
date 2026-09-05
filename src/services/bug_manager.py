from src.services.data_manager import add_data, load_data, save_data
from src.validators import validate_number


def add_bug(new_bug):
    bug_id_list = [bug["bug_id"] for bug in load_data()["bugs"]]
    if not new_bug.bug_id in bug_id_list:
        add_data(new_bug.to_dict())
    else:
        print("Bug with this ID is arleady in our system")


def choose_bug(action):
    while True:
        bugs_data = load_data()["bugs"]
        print("\n===============================")
        print("Active Bugs:")
        print("===============================")
        for bug in bugs_data:
            print(bug["bug_id"])
        picked_bug = input(f"Which Bug would you like to {action}? Pick by ID digits")
        if validate_number(picked_bug):
            for bug in bugs_data:
                if f"BG-{picked_bug}" == bug["bug_id"]:
                    return bug
            print("Picked bug does not exist, pick one from the list")


def display_bug():
    bug = choose_bug("display")
    print("\n===============================")
    print(f"Title: {bug['title']}")
    print(f"ID: {bug['bug_id']}")
    print(f"Status: {bug['status']}")
    print(f"Priority: {bug['priority']}")
    print(f"Description: {bug['description']}")
    print(f"Assigned to: {bug['assigned_to']}")
    print(f"Reported by: {bug['reported_by']}")
    print("\n===============================")


def delete_bug():
    bugs_data = load_data()
    bug = choose_bug("delete")
    bugs_data["bugs"].remove(bug)
    save_data(bugs_data)


def update_bug(single_bug, bug_field, new_value):
    data = load_data()
    for bug in data["bugs"]:
        if single_bug["bug_id"] == bug["bug_id"]:
            bug[bug_field] = new_value
    save_data(data)
