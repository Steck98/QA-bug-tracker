from src.services.data_manager import add_data, load_data


def add_employee(new_employee):
    if load_data() != None:
        employee_id_list = [
            employee["employee_id"] for employee in load_data()["users"]
        ]
        if not new_employee.employee_id in employee_id_list:
            add_data(new_employee.to_dict())
        else:
            print("employee with this ID is arleady in our system")
