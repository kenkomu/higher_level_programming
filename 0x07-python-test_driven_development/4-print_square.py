#!/usr/bin/python3

"""print_square module"""


def print_square(size):
    """print_square function

    prints a square with the character #.

    Attributes:
        size = square size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    for y in range(size):
        [print("#", end='') for x in range(size)]
        print()
    if size == 0:
        print()
