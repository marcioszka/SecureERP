from model.crm import crm
from view import terminal as view


def list_customers():
    crm_db = crm.data_manager.read_table_from_file(crm.DATAFILE)
    view.print_table(crm_db)


def add_customer():
    crm_db = crm.data_manager.read_table_from_file(crm.DATAFILE)
    user_input = view.get_inputs(crm.HEADERS)
    crm_db.append(user_input)
    crm.data_manager.write_table_to_file("crm.csv", crm_db)
    view.print_message(f"Customer {user_input[0]} added to database!")


def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    crm_db = crm.data_manager.read_table_from_file(crm.DATAFILE)
    delete_id = view.get_input("Select ID of customer to remove")
    for record in crm_db:
        if delete_id in record[0]:
            crm_db.remove(record)
            crm.data_manager.write_table_to_file(crm.DATAFILE, crm_db)
            view.print_message(
                f"Customer with ID {delete_id} has been removed!")
            return
    view.print_error_message(
        f"Customer with ID {delete_id} was not found!")


def get_subscribed_emails():
    crm_db = crm.data_manager.read_table_from_file(crm.DATAFILE)
    email_list = []
    for client in crm_db:
        if client[3] == "1":
            email_list.append(client[2])
    view.print_general_results(email_list, "Emails subscribed to newsletter:")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
