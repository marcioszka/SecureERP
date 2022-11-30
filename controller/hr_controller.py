from model.hr import hr
from view import terminal as view
from datetime import timedelta, date


def list_employees():
    ### view.print_error_message("Not implemented yet.")
    person=hr.read_from_file()
    view.print_table(person)
    
def add_employee():
    ### view.print_error_message("Not implemented yet.")
    id = view.get_input("Please provide the ID: ")
    person = view.get_input("Please provide the name: ")
    birthdays = view.get_input("Please provide birthday date: ")
    department = view.get_input("Please provide the department: ")
    clearance = view.get_input("Please provide the clearance: ")

    hr.create_file(id,person,birthdays,department,clearance)

def update_employee():
    ### view.print_error_message("Not implemented yet.")
    id = view.get_input("Please provide the ID: ")
    person = view.get_input("Please provide the name: ")
    birthdays = view.get_input("Please provide birthday date: ")
    department = view.get_input("Please provide the department: ")
    clearance = view.get_input("Please provide the clearance: ")

    hr.update_file(id,person,birthdays,department,clearance)

def delete_employee():
    ### view.print_error_message("Not implemented yet.")
    id = view.get_input("Please provide ID to remove permanently: ")
    hr.delete_from_file(id)


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    hr_db = hr.data_manager.read_table_from_file(hr.DATAFILE)
    birthdays = []
    dates = []
    date_from = date.today()
    user_date = view.get_input(
        "Input a date in format YYYY-MM-DD or leave blank  for today:")
    if len(user_date) == 10:
        date_from = date.fromisoformat(user_date)
    for num in range(14):
        dates.insert(num, (date_from + timedelta(num)))
    for person in hr_db:
        for test_date in dates:
            if person[2][4:] in date.isoformat(test_date)[4:]:
                birthdays.append(person)
    view.print_table(birthdays, hr.HEADERS)


def count_employees_with_clearance():
    hr_db = hr.data_manager.read_table_from_file(hr.DATAFILE)
    clearance_count = {}
    for record in hr_db:
        try:
            clearance_count[record[4]] += 1
        except KeyError:
            clearance_count.update({record[4]: 1})
    view.print_general_results(
        clearance_count, "Employees with clearance level:")


def count_employees_per_department():
    hr_db = hr.data_manager.read_table_from_file(hr.DATAFILE)
    department_count = {}
    for record in hr_db:
        try:
            department_count[record[3]] += 1
        except KeyError:
            department_count.update({record[3]: 1})
    view.print_general_results(
        department_count, "Employees in departments:")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
