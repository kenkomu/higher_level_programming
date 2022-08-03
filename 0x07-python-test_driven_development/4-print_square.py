#!/usr/bin/python3

"""print_square module"""


def print_square(size):
    """ print_square function
    this function print a square
    Attributes:
        size: square size
    """
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for y in range(size):
        [print("#", end='') for x in range(size)]
        print()
    if size == 0:
        print()
