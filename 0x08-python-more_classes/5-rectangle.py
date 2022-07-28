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

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (2*(self.__height + self.__width))

    def __str__(self):
        result = ""

        if(self.__height == 0) or (self.__width == 0):
            result += ''
        else:
            for row in range(self.height):
                result += "#" * self.width
                if (row < self.height - 1):
                    result += '\n'
        return result

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
