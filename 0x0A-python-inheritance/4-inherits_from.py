#!/usr/bin/python3
""" inherits_from module """


def inherits_from(obj, a_class):
    """ inherits_from function """
    return (
        type(obj) is not a_class and
        issubclass(type(obj), a_class)
    )
