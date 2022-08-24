#!/usr/bin/python3
"""save_to_json module"""


import json


def save_to_json_file(my_obj, filename):
    """
        function that writes an Object to a text file
        Args:
            filename: name of the file
            my_obj: object to append
    """
    with open('filename', mode='w') as file:
        json.dump(my_obj, file)
    file.closed
