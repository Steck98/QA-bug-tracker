from services.data_manager import *


def add_bug(new_bug):
    bug_id_list = [bug["bug_id"] for bug in load_data()["bugs"]]
    if not new_bug.bug_id in bug_id_list:
        add_data(new_bug.to_dict())
    else:
        print("Bug with this ID is arleady in our system")
