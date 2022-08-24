#!/usr/bin/python3
""" save_to_json_file module """


import json


def save_to_json_file(my_obj, filename):
    """
        function to save an object to a file
        Args:
            my_obj: object
            fileName: name of the file
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
    file.closed
