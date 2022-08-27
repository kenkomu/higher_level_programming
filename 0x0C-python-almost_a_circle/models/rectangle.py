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
        Base.strict_integer("width", width)
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        Base.strict_integer("height", height)
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        Base.strict_integer("x", x)
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        Base.strict_integer("y", y)
        self.__y = y
