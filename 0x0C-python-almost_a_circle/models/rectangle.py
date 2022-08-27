#!/usr/bin/python3
""" rectangle module """

from models.base import Base

class Rectangle:
    __height = None
    __width = None
    __x = None
    __y = None
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Private instance

        Args:
            width:width
            height:height
            x:x
            y:y
            id:id
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, width):
        self.width = width

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        self.height = height

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, x):
        self.x = x

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, y):
        self.y = y
