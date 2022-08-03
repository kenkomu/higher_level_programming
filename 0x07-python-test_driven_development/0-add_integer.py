#!/usr/bin/python3
def add_integer(a, b=98):
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if a != isinstance(a, int):
        raise TypeError
        print("a must be an integer")
    if b != isinstance(b, int):
        raise TypeError
        print("b must be an integer")
    return a + b
