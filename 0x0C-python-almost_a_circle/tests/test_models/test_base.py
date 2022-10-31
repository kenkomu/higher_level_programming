#!/usr/bin/python3
""" BaseTest module """


from models.base import Base
import unittest


class BaseTest(unittest.TestCase):
    """ BaseTest class """

    def testClassDocumentation(self):
        """
            Class have documentation
        """
        self.assertGreater(len(Base.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor have documentation
        """
        self.assertGreater(len(Base.__init__.__doc__), 0)

    def testInitId(self):
        """
            Function that test object id initialization at creation
        """
        Base.__nb_objects = 0

        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        b6 = Base("Holberton")
        b7 = Base(-4)
        b8 = Base(3.7)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, "Holberton")
        self.assertEqual(b7.id, -4)
        self.assertEqual(b8.id, 3.7)

    def testJsonToString(self):
        json = Base.to_json_string(None)
        self.assertEqual(json, "[]")
