def print_menu(title, list_options):
    i = 1
    print(title)
    for option in list_options[1:]:
        print(f"({i}) {option}")
        i += 1
    print(f"(0) {list_options[0]}")


def print_message(message):
    print(message)


def print_general_results(result, label):
    print(label)
    if isinstance(result, dict):
        for key, value in result.items():
            try:
                temp_value = '{:.2f}'.format(float(value))
                print(f"{key}: {temp_value}")
            except ValueError:
                print(f"{key}: {value}")
    elif isinstance(result, list or tuple):
        for element in result:
            try:
                temp_element = '{:.2f}'.format(float(element))
                print(temp_element)
            except ValueError:
                print(element)
    else:
        try:
            temp_result = '{:.2f}'.format(float(result))
            print(temp_result)
        except ValueError:
            print(result)
    print()


def print_table(table, headers):
    row_length = 0
    longest_string = []
    table.insert(0, headers)
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
    print()


def get_input(label):
    user_input = input(label + "\n")
    print()
    return user_input


def get_inputs(labels):
    user_input = []
    for label in labels:
        user_input.append(input(label + ":\n"))
    return user_input


def print_error_message(message):
    print(f"Error: {message}")
