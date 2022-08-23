#!/usr/bin/python3
""" Square class """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Constructor function """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Area function """
        return super().area()

    def __str__(self):
        """ Area function """
        return "[Square] {}/{}".format(self.__size, self.__size)
