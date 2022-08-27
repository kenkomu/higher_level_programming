#!/usr/bin/python3
""" Base module """

class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Constructor

        Args:
            id:id
        """
        if id == None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
