#!/usr/bin/python3
"""student module"""


class Student:
    """Student class"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Instantiation function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        function to generate a json from an object
        Args:
            obj: object
        """
        return self.__dict__
