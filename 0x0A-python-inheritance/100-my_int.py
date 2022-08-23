#!/usr/bin/python3
""" MyInt module """


class MyInt(int):
    """MyInt class"""

    def __ne__(self, Object):
        """ not equals function """
        return not self.__eq__(Object)

    def __eq__(self, object):
        """equals function """
        return super() == object
