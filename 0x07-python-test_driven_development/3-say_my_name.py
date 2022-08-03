#!/usr/bin/python3

"""say_my_name module"""


def say_my_name(first_name, last_name=""):
    """say_my_name function

    prints My name

    args:
        first_name = the first name
        last_name = the last name
    """

    if not isinstance(first_name, str):
        raise TypeError(
            "first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError(
            "last_name must be a string")
    print("My name is {:d} {:d}".format(first_name, last_name))
