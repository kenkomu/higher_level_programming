#!/usr/bin/python3
""" Square module """


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

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
            prmWidth=size,
            prmHeight=size,
            prmX=x,
            prmY=y,
            prmId=id
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
        Base.strict_integer_validation("size", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            Function that assigns an argument to each attribute
            Args:
                args: argument's array
                kwargs: argument's dictionary
        """
        if len(args) > 0:
            if len(args) > 0:
                self.strict_integer_validation("id", args[0])
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.strict_integer_validation("id", kwargs["id"])
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
            Function that returns the dictionary representation of the instance
        """
        return {"x": self.x, "y": self.y, "id": self.id, "size": self.size}
