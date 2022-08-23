#!/usr/bin/python3
"""base_geometry module"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """ area function """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator function """
        if (isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
