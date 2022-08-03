#!/usr/bin/python3
def add_integer(a, b=98):
    if isinstance(a, float, int):
        a = int(a)
        raise TypeError
        print("a must be an integer")
    if isinstance(a, float, int):
        b = int(b)
        raise TypeError
        print("b must be an integer")

    return a + b
