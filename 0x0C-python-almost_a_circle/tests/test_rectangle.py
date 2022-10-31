#!/usr/bin/python3
"""
    Unit test for Rectangle
"""

import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
        tests for Rectangle
    """
    def test_weight_is_integer(self):
        """
            test weight is int
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r3.width, 10)
        with self.assertRaises(ValueError):
            Rectangle(-2, 4)
        with self.assertRaises(TypeError):
            Rectangle(2.3, 5)
        with self.assertRaises(TypeError):
            Rectangle(None, 2)
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 2)
        with self.assertRaises(TypeError):
            Rectangle("abc", 2)
        with self.assertRaises(TypeError):
            Rectangle({1, 2}, 2)

    def test_height_is_integer(self):
        """
            test height is int
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r3.height, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, -4)
        with self.assertRaises(TypeError):
            Rectangle(2, 5.3)
        with self.assertRaises(TypeError):
            Rectangle(2, None)
        with self.assertRaises(TypeError):
            Rectangle(2, float('inf'))
        with self.assertRaises(TypeError):
            Rectangle(10, "hello", 2, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, {1, 2}, 0, 0, 12)

    def test_x_is_integer(self):
        """
            test x is int
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2, 3, 0, 12)

        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3.5, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, None, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, float('inf'), 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, (1, 2), 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "hello", 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {1, 2}, 0, 12)

    def test_y_is_integer(self):
        """
            test y is int
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2, 3, 2, 12)

        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -2, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, 2.6, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, None, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, float('inf'), 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, (1, 2, 3), 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "hello", 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, {1, 2}, 12)

    def test_area(self):
        """
            test the calculation of the area
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 3, 3, 2, 12)

        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 30)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -2, 0, 0, 12)
            r3.area()
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, 3, 3, 2, 12)
            r4.area()


"""
Unit test for the class Base and Rectangle
"""


class TestArea(unittest.TestCase):
    """ test area for class rectangle.py """
    def test_area_rectangle1(self):
        """ test with 2 integers """
        a = Rectangle(3, 5)
        self.assertEqual(a.area(), 15)

    def test_area_rectangle2(self):
        """ test with float for width and int for height"""
        with self.assertRaises(TypeError):
            a = Rectangle(0.3, 5)
            a.area()

    def test_area_rectangle3(self):
        """ test with int for width and float for heigt """
        with self.assertRaises(TypeError):
            a = Rectangle(3, 0.5)
            a.area()

    def test_area_rectangle4(self):
        """ test with 0 for width and int for height """
        with self.assertRaises(ValueError):
            a = Rectangle(0, 5)
            a.area()

    def test_area_rectangle5(self):
        """ test with int for widht and 0 for height """
        with self.assertRaises(ValueError):
            a = Rectangle(3, 0)
            a.area()

    def test_area_rectangle6(self):
        """ test for negative for width and int for height """
        with self.assertRaises(ValueError):
            a = Rectangle(-3, 5)
            a.area()

    def test_area_rectangle7(self):
        """ test with negative for width & height """
        with self.assertRaises(ValueError):
            a = Rectangle(-3, -5)
            a.area()

    def test_area_rectangle8(self):
        """ test with 1 arg """
        with self.assertRaises(TypeError):
            a = Rectangle(3)
            a.area()

    def test_area_rectangle9(self):
        """ test without arg """
        with self.assertRaises(TypeError):
            a = Rectangle()
            a.area()

    def test_area_rectangle10(self):
        """ test with arg None """
        with self.assertRaises(TypeError):
            a = Rectangle(None)
            a.area()

    def test_area_rectangle11(self):
        """ test with function for width and int for height """
        with self.assertRaises(UnboundLocalError):
            a = Rectangle(a.area(), 6)
            a.area()

    def test_area_rectangle12(self):
        """ test with strings """
        with self.assertRaises(TypeError):
            a = Rectangle("Hello!", "World")
            a.area()

    def test_area_rectangle13(self):
        """ test with tuples """
        with self.assertRaises(TypeError):
            a = Rectangle((1, 2, 3), (1, 2, 3))
            a.area()

    def test_area_rectangle14(self):
        """ test with lists """
        with self.assertRaises(TypeError):
            a = Rectangle([1, 2, 3], [1, 2, 3])
            a.area()

    def test_area_rectangle15(self):
        """ test with dictionaries """
        with self.assertRaises(TypeError):
            a = Rectangle({1, 2, 3}, {1, 2, 3})
            a.area()

    def test_area_rectangle16(self):
        """ test with float("inf") for width """
        with self.assertRaises(TypeError):
            a = Rectangle(float("inf"), 3)
            a.area()

    def test_area_rectangle17(self):
        """ test float("Nan") for width """
        with self.assertRaises(TypeError):
            a = Rectangle(float("NaN"), 5)
            a.area()

    def test_area_rectangle18(self):
        """ test with None for args """
        with self.assertRaises(TypeError):
            a = Rectangle(None, None)
            a.area()

    def test_area_rectangle19(self):
        """ test with string for width int for height """
        with self.assertRaises(TypeError):
            a = Rectangle("Hello!", 5)
            a.area()

    def test_area_rectangle20(self):
        """ test with int for width string for height """
        with self.assertRaises(TypeError):
            a = Rectangle(3, "World")
            a.area()

    def test_area_rectangle21(self):
        """ test with 1 string """
        with self.assertRaises(TypeError):
            a = Rectangle("Hello!")
            a.area()

    def test_area_rectangle22(self):
        """ test with 1 string """
        with self.assertRaises(TypeError):
            a = Rectangle.area()


class TestRectangle_Dict_Str(unittest.TestCase):
    """class testing the to_dictionary method and __str__ of Rectangle"""
    def test_to_dictionary(self):
        """test the to_dictionary method"""
        Base._Base__nb_objects = 0
        a = Rectangle(6, 2)
        output = {'id': 1, 'width': 6, 'height': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(1, 3, 5)
        output = {'id': 2, 'width': 1, 'height': 3, 'x': 5, 'y': 0}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(4, 4, 1, 6)
        output = {'id': 3, 'width': 4, 'height': 4, 'x': 1, 'y': 6}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(2, 7, 4, 2, 18)
        output = {'id': 18, 'width': 2, 'height': 7, 'x': 4, 'y': 2}
        self.assertDictEqual(a.to_dictionary(), output)

    def test_str(self):
        """test the output of the instance when printed"""
        Base._Base__nb_objects = 0
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print(Rectangle(4, 8))
        assert fake_stdout.getvalue() == '[Rectangle] (1) 0/0 - 4/8\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print(Rectangle(1, 3, 5, 7, 12))
        assert fake_stdout.getvalue() == '[Rectangle] (12) 5/7 - 1/3\n'

    def test_exception(self):
        """test with exception"""
        a = Rectangle(1, 2, 3, 4, 6)
        self.assertRaises(TypeError, a.to_dictionary, 0)
        a = Rectangle(1, 2)
        self.assertRaises(TypeError, a.to_dictionary, None)


class TestRectangleInit(unittest.TestCase):
    """
        tests for Rectangle
    """

    def test_rectangle_is_instance_of_base(self):
        """Test if the Rect is an instance of base
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertIsInstance(r1, Base)

    def test_value_is_int(self):
        """Test if the value for init is an int
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("f", "f", "f", "f", "f")

    def test_value_is_negativ(self):
        """test if value is neg
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, -2, -2, -0, -12)

    def test_value_is_x_heigt_not_neg(self):
        """test if x and x is not neg
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 0, -2, -0, -12)

    def test_value_is_x_neg(self):
        """test if x neg
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 10, 1, -1, 12)

    def test_value_is_not_tuple(self):
        """test W and H with tuples
        """
        with self.assertRaises(TypeError):
            r2 = Rectangle(3, 2, 2, (1, -10), 12)

    def test_y_is_not_tuple(self):
        """test X and Y with tuples
        """
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, -10, -2, (1, 10) - 12)

    def test_value_is_not_list(self):
        """test W and H with list
        """
        with self.assertRaises(TypeError):
            r2 = Rectangle(3, 2, 2, [1, -10], 12)

    def test_value_is_not_dict(self):
        """test W with dict
        """
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 2, 2, {'lolo': -10}, 12)

    def test_value_is_not_empty(self):
        """test empy instance
        """
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_display_None(self):
        """test with None
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None, None, None)

    def test_x_setter(self):
        """Test x setter"""
        r = Rectangle(5, 7, 0, 0, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_setter(self):
        """Test y setter"""
        r = Rectangle(5, 7, 30, 30, 10)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_x_setter_neg(self):
        """Test x setter neg"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 7, 30, 30, 1)
            r.x = -10

    def test_y_setter_neg(self):
        """Test y setter negative"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 7, 10, 30, 1)
            r.y = -10

    def test_x_setter_string(self):
        """Test x setter string"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 0, 0, 1)
            r.x = "lolo"

    def test_y_setter_string(self):
        """Test y setter string"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 0, 0, 1)
            r.y = "lolo"

    def test_x_setter_empty(self):
        """Test x empty"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 0, 0, 1)
            r.x = None

    def test_y_setter_empty(self):
        """Test y empty"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 0, 0, 1)
            r.y = None

    def test_x_setter_tuple(self):
        """Test x tuple"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 0, 0, 1)
            r.x = (1, 2)

    def test_y_setter_tuple(self):
        """Test y tuple"""
        r = Rectangle(1, 7, 0, 0, 1)
        with self.assertRaises(TypeError):
            r.y = (1, 2)

    def test_x_getter(self):
        """Test x getter"""
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(4, rect.x)

    def test_y_getter(self):
        """Test y getter"""
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(5, rect.y)


class TestRectangle_setter_getter(unittest.TestCase):
    """test getter setter of the rectangle height and width"""
    def test_height_getter(self):
        """test for the getter of the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(3, rect.height)

    def test_height_setter(self):
        """test to set an int to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.height = 12
        self.assertEqual(12, rect.height)

    def test_height_setter_negative(self):
        """test to set a negative int to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            rect.height = -12

    def test_height_setter_float(self):
        """test to set a float to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = 1.2

    def test_height_setter_string(self):
        """test to set a string to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = "ok"

    def test_height_setter_list(self):
        """test to set a list to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = [12]

    def test_height_setter_tuple(self):
        """test to set a tuple to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = (1, 2)

    def test_height_setter_dict(self):
        """test to set a dictonary to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = {12}

    def test_width_getter(self):
        """test for the getter of the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(2, rect.width)

    def test_width_setter(self):
        """test to set an int to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.width = 12
        self.assertEqual(12, rect.width)

    def test_width_setter_negative(self):
        """test to set a negative int to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            rect.width = -12

    def test_width_setter_float(self):
        """test to set a float to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.width = 1.2

    def test_width_setter_string(self):
        """test to set a string to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.width = "ok"

    def test_width_setter_list(self):
        """test to set a list to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.width = [12]

    def test_width_setter_tuple(self):
        """test to set a tuple to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.width = (1, 2)

    def test_width_setter_dict(self):
        """test to set a dictionary to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.width = {12}


if __name__ == '__main__':
    unittest.main()
