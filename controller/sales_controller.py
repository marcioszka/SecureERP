from model.sales import sales
from view import terminal as view
from datetime import date, timedelta


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
    view.print_error_message("Not implemented yet.")


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
