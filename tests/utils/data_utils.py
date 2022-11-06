import random
import string


def get_random_string(length: int) -> str:
    """Return random string with length-size"""
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


def str_generator(n: int):
    """Random csv-like data generator"""

    string_size = 10

    while True:
        if n == 0:
            break
        yield get_random_string(string_size)
        n -= 1


def int_generator(n: int):
    """Random csv-like data generator"""

    while True:
        if n == 0:
            break
        yield random.randint(-1000, 1000)
        n -= 1
