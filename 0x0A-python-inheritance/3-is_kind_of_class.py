#!/usr/bin/python3
"""is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class function"""
    return type(obj) or obj is a_class
