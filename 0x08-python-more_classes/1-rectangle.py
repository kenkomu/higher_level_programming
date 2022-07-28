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

    def __init__(self, wwidth=0, hheight=0):
        self.width = wwidth
        self.height = hheight

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, wwidth):
        if not isinstance(wwidth, int):
            raise TypeError("width must be an integer")
        if wwidth < 0:
            raise ValueError("width must be >= 0")
        self.__width = wwidth

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, hheight):
        if not isinstance(hheight, int):
            raise TypeError("height must be an integer")
        if hheight < 0:
            raise ValueError("height must be >= 0")
        self.__height = hheight
