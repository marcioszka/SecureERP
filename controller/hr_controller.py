from model.hr import hr
from view import terminal as view
from datetime import timedelta, date


def list_employees():
    hr_db = hr.data_manager.read_table_from_file(hr.DATAFILE)
    view.print_table(hr_db, hr.HEADERS)


def add_employee():
    hr_db = hr.data_manager.read_table_from_file(hr.DATAFILE)
    new_employee = view.get_inputs(hr.HEADERS)
    hr_db.append(new_employee)
    hr_db.data_manager.write_table_to_file(hr.DATAFILE, hr_db)
    view.print_message(
        f"New employee {new_employee[0]} has been added to the database")


def update_employee():
    hr_db = hr.data_manager.read_table_from_file(hr.DATAFILE)
    id_employee_to_update = view.get_input("Select ID of a employee to update")
    updated_employee = []
    for data in hr_db:
        if data[0] == id_employee_to_update:
            updated_detail = view.get_inputs(hr.HEADERS)
            updated_data = updated_detail
        else:
            updated_data = data
        updated_employee.append(updated_data)
    hr.data_manager.write_table_to_file(hr.DATAFILE, updated_employee)
    view.print_message(f"Employee {id_employee_to_update} has been updated.")


def delete_employee():
    hr_db = hr.data_manager.read_table_from_file(hr.DATAFILE)
    deleted_employee = view.get_input("Select ID of a employee to delete")
    for data in hr_db:
        if deleted_employee in data[0]:
            hr.remove(data)
            hr.data_manager.write_table_to_file(hr.DATAFILE, hr_db)
            view.print_message(
                f"Employee {deleted_employee} has been deleted from database")
        else:
            return view.print_error_message(f"Employee {deleted_employee} is not listed in a database.")


def get_oldest_and_youngest():
    hr_database = hr.data_manager.read_table_from_file(hr.DATAFILE)
    birthday_of_youngest, birthday_of_oldest = hr_database[0][2], hr_database[0][2]
    oldest_employee_name, youngest_employee_name = hr_database[0][1], hr_database[0][1]
    for data in hr_database:
        if data[2] < birthday_of_oldest:
            birthday_of_oldest = data[2]
            oldest_employee_name = data[1]
        if data[2] > birthday_of_youngest:
            birthday_of_youngest = data[2]
            youngest_employee_name = data[1]
    oldest_and_youngest = oldest_employee_name, youngest_employee_name
    view.print_message(
        f"Oldest and youngest employees are respectively {', '.join(oldest_and_youngest)}.")


def get_average_age():
    hr_db = hr.data_manager.read_table_from_file(hr.DATAFILE)
    ages = []
    today = date.today()
    for person in hr_db:
        birth_date = date.fromisoformat(person[2])
        years = today.year - birth_date.year
        if all((x >= y) for x, y in zip(today.timetuple(),
                                        birth_date.timetuple())):
            ages.append(years)
        else:
            ages.append(years - 1)
    view.print_general_results(
        int(sum(ages) / len(ages)), "Average employee age:")


def next_birthdays():
    hr_db = hr.data_manager.read_table_from_file(hr.DATAFILE)
    birthdays = []
    dates = []
    date_from = date.today()
    user_date = view.get_input(
        "Input a date in format YYYY-MM-DD or leave blank for today:")
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
