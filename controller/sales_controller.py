from model.sales import sales
from view import terminal as view
from datetime import date, timedelta


def list_transactions():
    sales_database = sales.data_manager.read_table_from_file(sales.DATAFILE)
    view.print_table(sales_database, sales.HEADERS)


def add_transaction():
    sales_database = sales.data_manager.read_table_from_file(sales.DATAFILE)
    used_transaction_id = []
    for sale in sales_database:
        used_transaction_id.append(sale[0])
    new_transaction_id = sales.util.generate_id()
    while new_transaction_id in used_transaction_id:
        new_transaction_id = sales.util.generate_id()
    new_transaction = view.get_inputs(sales.HEADERS[1:])
    new_transaction.insert(0, new_transaction_id)
    sales_database.append(new_transaction)
    sales.data_manager.write_table_to_file(sales.DATAFILE, sales_database)
    view.print_message(f"Transaction {new_transaction[0]} added to database!")


def update_transaction():
    sales_database = sales.data_manager.read_table_from_file(sales.DATAFILE)
    id_transaction_to_update = view.get_input(
        "Select ID of a transaction to update")
    updated_sales = []
    for data in sales_database:
        if data[0] == id_transaction_to_update:
            updated_detail = view.get_inputs(sales.HEADERS)
            updated_data = updated_detail
        else:
            updated_data = data
        updated_sales.append(updated_data)
    sales.data_manager.write_table_to_file(sales.DATAFILE, updated_sales)
    view.print_message(
        f"Transaction {id_transaction_to_update} has been updated.")


def delete_transaction():
    sales_database = sales.data_manager.read_table_from_file(sales.DATAFILE)
    deleted_transaction = view.get_input(
        "Select ID of a transaction to delete")
    #if deleted_transaction not in sales_database:
    #    view.print_error_message(f"Transaction {deleted_transaction} is not listed in a database.")
    for data in sales_database:
        if deleted_transaction in data[0]:
            sales_database.remove(data)
            sales.data_manager.write_table_to_file(
                sales.DATAFILE, sales_database)
            return view.print_message(
                f"Transaction {deleted_transaction} deleted from database.")
    view.print_error_message(f"Transaction {deleted_transaction} is not listed in a database.")
    

def get_biggest_revenue_transaction():
    # Exits sales menu
    sales_db = sales.data_manager.read_table_from_file(sales.DATAFILE)
    data = {}
    largest_transaction = 0.0
    data_list = [[]]
    for transaction in sales_db:
        if float(transaction[3]) > largest_transaction:
            i = 0
            largest_transaction = float(transaction[3])
            for item in transaction:
                data.update({sales.HEADERS[i]: item})
                i += 1
    for value in data.values():
        data_list[0].append(value)
    view.print_table(data_list, sales.HEADERS)


def get_biggest_revenue_product():
    # Exits sales menu
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
    view.print_general_results(
        {item_name: sales_sum}, "Product that made the highest revenue overall:")


def count_transactions_between():
    starting_date = view.get_input(
        "Enter a starting date in YYYY-MM-DD format with which database is searched.")
    ending_date = view.get_input(
        "Enter an ending date in YYYY-MM-DD format with which database is searched.")
    transaction_counter = 0
    sales_database = sales.data_manager.read_table_from_file(sales.DATAFILE)
    for data in sales_database:
        if data[4] >= starting_date and data[4] <= ending_date:
            transaction_counter += 1
    if transaction_counter == 0:
        view.print_message(
            f"There have been no transactions between {starting_date} and {ending_date}.")
    elif transaction_counter == 1:
        view.print_message(
            f"There has been {transaction_counter} transaction between {starting_date} and {ending_date}.")
    else:
        view.print_message(
            f"There have been {transaction_counter} transactions between {starting_date} and {ending_date}.")


def sum_transactions_between():
    start_date = view.get_input("Start date in format YYYY-MM-DD:")
    end_date = view.get_input("End date in format YYYY-MM-DD:")

    def dates_between(start_date, end_date):
        dates_list = []
        for iso_date in range(int((end_date - start_date).days)+1):
            day = start_date + timedelta(iso_date)
            dates_list.append(day.strftime('%Y-%m-%d'))
        return dates_list
    sales_db = sales.data_manager.read_table_from_file(sales.DATAFILE)
    year_from, month_from, day_from = start_date.split("-")
    year_to, month_to, day_to = end_date.split("-")
    from_date = date(int(year_from), int(month_from), int(day_from))
    to_date = date(int(year_to), int(month_to), int(day_to))
    dates = dates_between(from_date, to_date)
    transaction_sum = 0.0
    for transaction in sales_db:
        if transaction[4] in dates:
            transaction_sum += float(transaction[3])
    view.print_general_results(
        transaction_sum, f"Sum of transactions between {start_date} - {end_date}:")


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
