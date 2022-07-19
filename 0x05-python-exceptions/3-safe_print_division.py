#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = int(a) / int(b)
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {:d}".format(result))
        return result
