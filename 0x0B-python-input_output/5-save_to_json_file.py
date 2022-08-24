#!/usr/bin/python3
"""save_to_json module"""

import json


def save_to_json_file(my_obj, filename):
    with open('filename', mode='w') as file:
        json.dump(my_obj, file)
