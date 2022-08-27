#!/usr/bin/python3
""" rectangle module """

from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    __height = None
    __width = None
    __x = None
    __y = None

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Private instance

        Args:
            id:id
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
