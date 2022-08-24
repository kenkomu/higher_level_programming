#!/usr/bin/python3
""" load_from_json_file module """


import json


def load_from_json_file(filename):
    """
        function load json from a file
        Args:
            filename: name of the file
    """
    obj = None
    with open(filename) as file:
        obj = json.load(file)
    file.closed
    return obj
