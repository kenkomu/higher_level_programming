#!/usr/bin/python3

"""
    Unittests for Base module
"""

import unittest
import os
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
        test for Base
    """
    def test_creation_id(self):
        """
            test if value of id has the good assignment
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(-5)
        b6 = Base(6.3)
        b7 = Base()
        b8 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, -5)
        self.assertEqual(b6.id, 6.3)
        self.assertEqual(b7.id, 4)
        self.assertEqual(b8.id, 5)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string(self):
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])


"""
    Unittest for Base Rectangle and Square pep8 documentation
"""


class TestBase(unittest.TestCase):
    """
        test for comments for base rectangle and square files
    """
    def test_conformance_base(self):
        """
            Test that we conform to PEP-8 for Base
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_conformance_rectangle(self):
        """
            Test that we conform to PEP-8 for Rectangle
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_conformance_square(self):
        """
            Test that we conform to PEP-8 for Square
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0)


"""
    Unittest for the create function of the Base class
"""


class Test_Base_Create(unittest.TestCase):
    """class test of the create base function"""

    def test_rectangle_create(self):
        """test rectangle creation"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_square_create(self):
        """test square creation"""
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)


"""
    Unittest for the init function of the Base class
"""


class Test_Base_Init(unittest.TestCase):
    """class test of the init base function"""

    def test_id_int(self):
        """Test integer id"""
        b = Base(5)
        self.assertEqual(b.id, 5)
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base(-3)
        self.assertEqual(b.id, -3)

    def test_id_incrementation(self):
        """Test id incrementation"""
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(7)
        self.assertEqual(b.id, 7)
        b = Base(None)
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)

    def test_id_non_int(self):
        """Test non integer id"""
        b = Base("Holberton")
        self.assertEqual(b.id, "Holberton")
        b = Base('A')
        self.assertEqual(b.id, 'A')
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))
        b = Base({"id": 7, "name": "Betty"})
        self.assertEqual(b.id, {"id": 7, "name": "Betty"})
        b = Base(False)
        self.assertEqual(b.id, False)

    def test_id_error(self):
        """Test error"""
        with self.assertRaises(TypeError):
            b = Base(1, 2)
        with self.assertRaises(TypeError):
            b = Base(1, None)


"""Unittests for to_json_string(list_dictionaries)"""


class TestToJsonString(unittest.TestCase):
    """Unittest for to_json_string"""
    def test_rectangle_to_str(self):
        """True if to_json_string return str type"""
        r1 = Rectangle(10, 7, 4, 6, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str, type(json_dictionary))

    def test_rectangle_instance(self):
        """Test rectangle instance with len()"""
        r1 = Rectangle(10, 7, 6, 4, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(len(json_dictionary) == 53)

    def test_more_rectangle_to_str(self):
        """True if to_json_string return str type"""
        r1 = Rectangle(10, 7, 4, 6, 1)
        r2 = Rectangle(7, 10, 6, 4, 1)
        dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertEqual(str, type(json_dictionary))

    def test_more_rectangle_instances(self):
        """Test rectangle instances with len()"""
        r1 = Rectangle(10, 7, 4, 6, 1)
        r2 = Rectangle(7, 10, 6, 4, 1)
        dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertTrue(len(json_dictionary) == 106)

    def test_square_to_str(self):
        """True if to_json_string return str type"""
        s1 = Square(10, 4, 6, 1)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(str, type(json_dictionary))

    def test_square_instance(self):
        """Test square instance with len()"""
        s1 = Square(10, 4, 6, 1)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string(dictionary)
        self.assertTrue(len(json_dictionary) == 37)

    def test_more_squares_to_str(self):
        """True if to_json_string return str type"""
        s1 = Square(10, 4, 6, 1)
        s2 = Square(7, 6, 4, 1)
        dictionaries = [s1.to_dictionary(), s2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertEqual(str, type(json_dictionary))

    def test_more_square_instances(self):
        """Test square instances with len()"""
        s1 = Square(10, 4, 6, 1)
        s2 = Square(7, 6, 4, 1)
        dictionaries = [s1.to_dictionary(), s2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertTrue(len(json_dictionary) == 77)

    def test_empty(self):
        """Test with empty value"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none(self):
        """Test with None"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_parameters(self):
        """Test if no parameter (list_dicitonaries)"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_parameters(self):
        """Test if more undefined parameters"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 3600)


"""
Unit test for the load_from_file method of the Base class
"""


class TestBaseSize(unittest.TestCase):
    """ tests for load_from_file of base.py """

    def test_load_empty_file(self):
        """Tests for non existant and empty file"""
        if (os.path.exists("Rectangle.json") is True):
            os.remove("Rectangle.json")
        if (os.path.exists("Square.json") is True):
            os.remove("Square.json")
        if (os.path.exists("Base.json") is True):
            os.remove("Base.json")
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])
        os.mknod("Rectangle.json")
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])

    def test_load_rectangle(self):
        """Test for loading a list of rectangles"""
        rect_a = Rectangle(2, 4)
        rect_b = Rectangle(1, 1)
        rect_c = Rectangle(6, 6)
        my_list = [rect_a, rect_b, rect_c]
        Rectangle.save_to_file([rect_a, rect_b, rect_c])
        my_list_loaded = Rectangle.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Rectangle.json")

    def test_load_square(self):
        """Test for loading a list of squares"""
        rect_a = Square(2)
        rect_b = Square(1)
        rect_c = Square(6)
        my_list = [rect_a, rect_b, rect_c]
        Square.save_to_file([rect_a, rect_b, rect_c])
        my_list_loaded = Square.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Square.json")

    def test_extra_args(self):
        """Test calling the function with an additional argument"""
        with self.assertRaises(TypeError):
            Base.load_from_file("Hello")


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    def test_save_one_rectangle(self):
        """test for one rectangle"""
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_save_two_rectangles(self):
        """test for two rectangles"""
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_one_square(self):
        """test for one square"""
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_two_squares(self):
        """test for two squares"""
        square1 = Square(10, 7, 2, 8)
        square2 = Square(8, 1, 2, 3)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)

    def test_save_overwrite(self):
        """test for overwrite"""
        square = Square(8, 5, 9, 2)
        Square.save_to_file([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_empty_list(self):
        """test for an empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_no_args(self):
        """test for no argument"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_two_arg(self):
        """test for two arguments"""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


if __name__ == '__main__':
    unittest.main()
