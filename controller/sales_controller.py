from model.sales import sales
from view import terminal as view


def list_transactions():
    view.print_error_message("Not implemented yet.")


def add_transaction():
    view.print_error_message("Not implemented yet.")


def update_transaction():
    view.print_error_message("Not implemented yet.")


def delete_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_transaction():
    sales_db = sales.data_manager.read_table_from_file(sales.DATAFILE)
    data = {}
    largest_transaction = 0.0
    for transaction in sales_db:
        if float(transaction[3]) > largest_transaction:
            i = 0
            largest_transaction = float(transaction[3])
            for item in transaction:
                data.update({sales.HEADERS[i]: item})
                i += 1
    return data


def get_biggest_revenue_product():
    sales_db = sales.data_manager.read_table_from_file(sales.DATAFILE)
    data = {}
    item_name = ""
    sales_sum = 0.0
    for transaction in sales_db:
        try:
            data[transaction[2]] += float(transaction[3])
        except KeyError:
            data.update({transaction[2]: float(transaction[3])})
    for key, value in data.items():
        if float(value) > sales_sum:
            item_name, sales_sum = key, float(value)
    return {item_name: sales_sum}


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
