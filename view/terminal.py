def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    i = 1
    print(title)
    for option in list_options[1:]:
        print(f"({i}) {option}")
        i += 1
    print(f"(0) {list_options[0]}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    pass


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \--------------------------------/
def print_table(table, headers):
    row_length = 0
    longest_string = []
    for _ in headers:
        longest_string.append("")
    for person in table:
        i = 0
        for item in person:
            temp_string = f"{' ':<2}{item}{' ':>2}"
            if len(temp_string) > len(longest_string[i]):
                longest_string[i] = temp_string
            i += 1
    row_length = len('  '.join(longest_string)) + 1
    print(f"/{'-' * (row_length)}\\")
    for person in table:
        print("|", end="")
        i = 0
        for item in person:
            column_width = len(longest_string[i]) - len(item)
            if (column_width) % 2 == 0:
                width = column_width / 2
                print(
                    f"{'':<{width}}{item}{'':>{width + 1}}", end="")
            else:
                width = column_width / 2 + 0.5
                print(
                    f"{'':<{width}}{item}{'':>{width}}", end="")
            print("|", end="")
            i += 1

        print()
        if person != table[-1]:
            print(f"|{'-' * (row_length)}|")
        else:
            print(f"\\{'-' * (row_length)}/")


def get_input(label):
    user_input = input(label + "\n")
    print()
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    pass


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    pass
