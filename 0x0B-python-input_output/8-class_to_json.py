#!/usr/bin/python3
""" class_to_json module """


def class_to_json(obj):
    """
        function to generate a json from an object
        Args:
            obj: object
    """
    return obj.__dict__
