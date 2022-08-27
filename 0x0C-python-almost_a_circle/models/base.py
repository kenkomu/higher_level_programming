#!/usr/bin/python3
""" base module """


from termios import VLNEXT


class Base:
    """Base class"""
    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """
        Constructor

        Args:
            id:id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def strict_integer(name, value):
        """
            strict integer
            Args:
                name: name of the variable
                value: value of the variable
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def integer_validation(name, value):
        """
            strict integer
            Args:
                name: name of the variable
                value: value of the variable
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
