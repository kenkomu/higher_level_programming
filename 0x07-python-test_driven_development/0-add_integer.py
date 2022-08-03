#!/usr/bin/python3
def add_integer(a, b=98):
    if isinstance(a, float):
        a = int(a)
        raise TypeError
        print("a must be an integer")
    if isinstance(b, float):
        b = int(b)
        raise TypeError
        print("b must be an integer")
    
    return a + b
