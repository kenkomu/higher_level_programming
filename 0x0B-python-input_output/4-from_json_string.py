#!/usr/bin/python3
"""from_json_string module"""

import json


def from_json_string(my_str):
    """from_json_string function"""
    sorted = json.dumps(my_str, sort_keys=True)
    print(sorted)
