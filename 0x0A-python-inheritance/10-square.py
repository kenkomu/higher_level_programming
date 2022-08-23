#!/usr/bin/python3

""" Square module """

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """ Area function """
        return super().area()
