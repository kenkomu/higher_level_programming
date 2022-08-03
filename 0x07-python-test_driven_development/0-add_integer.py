#!/usr/bin/python3
"""add_integer module"""

def add_integer(a, b=98):
    """ add_integer function
    this function add two integer
    Attributes:
        prmA: first integer
        prmB: second integer
    """
    if isinstance(a, float):
        a = int(a)
        raise TypeError
        print("a must be an integer")
    if isinstance(b, float):
        b = int(b)
        raise TypeError
        print("b must be an integer")
    
    return a + b
