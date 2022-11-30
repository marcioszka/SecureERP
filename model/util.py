import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    small_letters = [*string.ascii_lowercase]
    capital_letters = [*string.ascii_uppercase]
    digits = [*string.digits]
    special_chars = [*allowed_special_chars]
    randomized_symbols = []
    for _ in range(number_of_small_letters):
        randomized_symbols.append(random.choice(small_letters))
    for _ in range(number_of_capital_letters):
        randomized_symbols.append(random.choice(capital_letters))
    for _ in range(number_of_digits):
        randomized_symbols.append(random.choice(digits))
    for _ in range(number_of_special_chars):
        randomized_symbols.append(random.choice(special_chars))
    random.shuffle(randomized_symbols)
    unique_id = ''.join(randomized_symbols)
    return unique_id
