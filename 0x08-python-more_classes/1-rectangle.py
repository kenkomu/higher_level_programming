#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """empty class Rectangle that defines a rectangle
    Attributes:
        width: width of the rectangle
        height: height of the rectangle
    """
    __width = 0
    __height = 0
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

