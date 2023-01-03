from functools import partial
import string


def num_to_power(num, power):
    return num ** power


square_power = partial(num_to_power, power=2)

lst = list(string.ascii_letters)

print(list(string.whitespace))
