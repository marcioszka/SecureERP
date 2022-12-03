from model.crm import crm
from view import terminal as view


def list_customers():
    crm_db = crm.get_table()
    view.print_table(crm_db, crm.HEADERS)


def add_customer():
    crm_db = crm.get_table()
    unique_id = crm.util.generate_id()
    used_ids = []
    for person in crm_db:
        used_ids.append(person[0])
    while unique_id in used_ids:
        unique_id = crm.util.generate_id()
    user_input = view.get_inputs(crm.HEADERS[1:])
    # new_user = unique_id + user_input
    user_input.insert(0, unique_id)
    crm_db.append(user_input)
    crm.write_file(crm_db)
    view.print_message(f"Customer {user_input[1]} added to database!")


def update_customer():
    crm_database = crm.get_table()
    id_customer_to_update = view.get_input(
        "Select an ID of a customer to update.")
    updated_crm = []
    for data in crm_database:
        if data[0] == id_customer_to_update:
            updated_customer = view.get_inputs(crm.HEADERS[1:])
            updated_data = updated_customer
            updated_data.insert(0, id_customer_to_update)
        else:
            updated_data = data
        updated_crm.append(updated_data)
    crm.write_file(updated_crm)
    view.print_message(
        f"Details of customer #{id_customer_to_update} have been updated.")


def delete_customer():
    crm_db = crm.get_table()
    view.print_table(crm_db, crm.HEADERS)
    delete_id = view.get_input("Select ID of customer to remove")
    for record in crm_db:
        if delete_id == record[0]:
            crm_db.remove(record)
            crm.write_file(crm_db)
            view.print_message(
                f"Customer with ID {delete_id} has been removed!")
            return
    view.print_error_message(
        f"Customer with ID {delete_id} was not found!")


def get_subscribed_emails():
    crm_db = crm.get_table()
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
