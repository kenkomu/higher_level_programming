#!/usr/bin/python3
"""Square class"""


class Square:
    """empty class Square that defines a square
    Attributes

    size: size of the square
    """
    __size = 0

    def __init__(self, ssize=0):
        self.__size = ssize

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, ssize=0):
        if not isinstance(ssize, int):
            raise TypeError("size must be an integer")
        if ssize < 0:
            raise ValueError("size must be >= 0")
        self.__size = ssize

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for y in range(self.size):
            [print("#", end="") for x in range(self.size)]
            print()
        if self.size == 0:
            print()
