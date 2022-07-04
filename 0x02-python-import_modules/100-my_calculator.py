#!/usr/bin/python3
from ast import operator
from unittest import result


if __name__ == "__main__":
    """
    Handle basic arithmetic operations.
    """
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) -1 !=3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a,b)
    elif operator == '/':
        result = mul(a/b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print(f"{a} {operator} {b} = {result}")
