#!/usr/bin/python3
"""add_integer module"""


def add_integer(a, b=98):
    """ add_integer function

    this function add two integer

    Attributes:
        a: first integer
        b: optional second integer (init by 98 by default)
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
