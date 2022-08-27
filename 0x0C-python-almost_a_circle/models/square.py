#!/usr/bin/python3
""" rectangle module """

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
            Constructor function
            Args:
                width:  width
                height: height
                x:      left margin
                y:      top margin
                id:     id
        """
        super().__init__(
            width=width
            height=height
            x=x
            y=y
            id=id
        )

    def __str__(self):
        """
            Function that return a string representation of the square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """ y getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        Base.strict_integer("size", value)
        self.width = value
        self.height = value
