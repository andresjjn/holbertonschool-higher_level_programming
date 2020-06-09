#!/usr/bin/python3
"""Unittest for Rectangle class from almost circle python project
"""
import unittest
import pep8
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class test_Rectangle(unittest.TestCase):
    """Class testing for Rectangle using unittest"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_types_constructor(self):
        """Public method to check types of data in constructor class method"""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Rectangle)
        with self.assertRaises(TypeError):
            r0 = Rectangle(None)
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None)
        with self.assertRaises(TypeError):
            r2 = Rectangle()
        with self.assertRaises(TypeError):
            r3 = Rectangle(3, 3, 3, 3, 3, 3, 3)
        with self.assertRaises(TypeError):
            r4 = Rectangle((3 + 5j), 8)
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, [8, 7])
        with self.assertRaises(TypeError):
            r6 = Rectangle(5.2, 6)
        with self.assertRaises(TypeError):
            r7 = Rectangle({'malo': 3, 'bueno': 6}, 6)
        with self.assertRaises(TypeError):
            r8 = Rectangle(True, 6)
        with self.assertRaises(TypeError):
            r9 = Rectangle((4, 3), 6)
        with self.assertRaises(TypeError):
            r10 = Rectangle("sY CiRbo", 6)
        with self.assertRaises(TypeError):
            r11 = Rectangle(([4, 3]), 6)
        with self.assertRaises(TypeError):
            r12 = Rectangle(8, (3 + 5j))
        with self.assertRaises(TypeError):
            r13 = Rectangle([8, 7], 5)
        with self.assertRaises(TypeError):
            r14 = Rectangle(5, 5.2)
        with self.assertRaises(TypeError):
            r15 = Rectangle(6, {'malo': 3, 'bueno': 6})
        with self.assertRaises(TypeError):
            r16 = Rectangle(6, True)
        with self.assertRaises(TypeError):
            r17 = Rectangle(6, (4, 3))
        with self.assertRaises(TypeError):
            r18 = Rectangle(6, "sY CiRbo")
        with self.assertRaises(TypeError):
            r19 = Rectangle(6, ([4, 3]))
        with self.assertRaises(TypeError):
            r20 = Rectangle(8, 5, (3 + 5j))
        with self.assertRaises(TypeError):
            r21 = Rectangle(5, 5, [8, 7])
        with self.assertRaises(TypeError):
            r22 = Rectangle(5, 5, 5.2)
        with self.assertRaises(TypeError):
            r23 = Rectangle(6, 4, {'malo': 3, 'bueno': 6})
        with self.assertRaises(TypeError):
            r24 = Rectangle(6, 4, True)
        with self.assertRaises(TypeError):
            r25 = Rectangle(6, 3, (4, 3))
        with self.assertRaises(TypeError):
            r26 = Rectangle(6, 5, "sY CiRbo")
        with self.assertRaises(TypeError):
            r27 = Rectangle(6, 9, ([4, 3]))
        with self.assertRaises(TypeError):
            r28 = Rectangle(8, 5, 4, (3 + 5j))
        with self.assertRaises(TypeError):
            r29 = Rectangle(5, 5, 3, [8, 7])
        with self.assertRaises(TypeError):
            r30 = Rectangle(5, 5, 4, 5.2)
        with self.assertRaises(TypeError):
            r31 = Rectangle(6, 4, 2, {'malo': 3, 'bueno': 6})
        with self.assertRaises(TypeError):
            r32 = Rectangle(6, 4, 5, True)
        with self.assertRaises(TypeError):
            r33 = Rectangle(6, 3, 9, (4, 3))
        with self.assertRaises(TypeError):
            r34 = Rectangle(6, 5, 6, "sY CiRbo")
        with self.assertRaises(TypeError):
            r35 = Rectangle(6, 9, 7, ([4, 3]))

    def test_values_constructor(self):
        """Public method to check types of data in constructor class method"""
        with self.assertRaises(ValueError):
            r20 = Rectangle(-2, 2, 2, 2, 2)
        with self.assertRaises(ValueError):
            r21 = Rectangle(2, -2, 2, 2, 2)
        with self.assertRaises(ValueError):
            r22 = Rectangle(0, 2, 2, 2, 2)
        with self.assertRaises(ValueError):
            r23 = Rectangle(2, 0, 2, 2, 2)
        with self.assertRaises(ValueError):
            r24 = Rectangle(2, 2, 0, -1, 2)
        with self.assertRaises(ValueError):
            r25 = Rectangle(2, 2, -1, 0, 2)
        with self.assertRaises(ValueError):
            r25 = Rectangle(2, 2, -1, 0, 2)

    def test_setters(self):
        """Public method to check types and values de getters methods"""
        r26 = Rectangle(2, 2)
        r26.width = 8
        self.assertEqual(r26.width, 8)
        self.assertEqual(type(r26.width), int)
        with self.assertRaises(TypeError):
            r26.width = (3 + 5j)
        with self.assertRaises(TypeError):
            r26.width = [5, 7]
        with self.assertRaises(TypeError):
            r26.width = 5.2
        with self.assertRaises(TypeError):
            r26.width = {'malo': 3, 'bueno': 6}
        with self.assertRaises(TypeError):
            r26.width = True
        with self.assertRaises(TypeError):
            r26.width = (5, 8)
        with self.assertRaises(TypeError):
            r26.width = "sY CiRbo"
        with self.assertRaises(TypeError):
            r26.width = ([4, 3])
        with self.assertRaises(ValueError):
            r26.width = (0)
        with self.assertRaises(ValueError):
            r26.width = (-1)

        r26.height = 8
        self.assertEqual(r26.height, 8)
        self.assertEqual(type(r26.height), int)
        with self.assertRaises(TypeError):
            r26.height = (3 + 5j)
        with self.assertRaises(TypeError):
            r26.height = [5, 7]
        with self.assertRaises(TypeError):
            r26.height = 5.2
        with self.assertRaises(TypeError):
            r26.height = {'malo': 3, 'bueno': 6}
        with self.assertRaises(TypeError):
            r26.height = True
        with self.assertRaises(TypeError):
            r26.height = (5, 8)
        with self.assertRaises(TypeError):
            r26.height = "sY CiRbo"
        with self.assertRaises(TypeError):
            r26.height = ([4, 3])
        with self.assertRaises(ValueError):
            r26.height = (0)
        with self.assertRaises(ValueError):
            r26.height = (-1)

        r26.x = 8
        self.assertEqual(r26.x, 8)
        self.assertEqual(type(r26.x), int)
        with self.assertRaises(TypeError):
            r26.x = (3 + 5j)
        with self.assertRaises(TypeError):
            r26.x = [5, 7]
        with self.assertRaises(TypeError):
            r26.x = 5.2
        with self.assertRaises(TypeError):
            r26.x = {'malo': 3, 'bueno': 6}
        with self.assertRaises(TypeError):
            r26.x = True
        with self.assertRaises(TypeError):
            r26.x = (5, 8)
        with self.assertRaises(TypeError):
            r26.x = "sY CiRbo"
        with self.assertRaises(TypeError):
            r26.x = ([4, 3])
        with self.assertRaises(ValueError):
            r26.x = (-1)

        r26.y = 8
        self.assertEqual(r26.y, 8)
        self.assertEqual(type(r26.y), int)
        with self.assertRaises(TypeError):
            r26.y = (3 + 5j)
        with self.assertRaises(TypeError):
            r26.y = [5, 7]
        with self.assertRaises(TypeError):
            r26.y = 5.2
        with self.assertRaises(TypeError):
            r26.y = {'malo': 3, 'bueno': 6}
        with self.assertRaises(TypeError):
            r26.y = True
        with self.assertRaises(TypeError):
            r26.y = (5, 8)
        with self.assertRaises(TypeError):
            r26.y = "sY CiRbo"
        with self.assertRaises(TypeError):
            r26.y = ([4, 3])
        with self.assertRaises(ValueError):
            r26.y = (-1)

        r26.id = 8
        self.assertEqual(r26.id, 8)
        self.assertEqual(type(r26.id), int)

    def test_area(self):
        """Public method to check area method"""
        r27 = Rectangle(2, 2)
        self.assertEqual(r27.area(), 4)
        self.assertEqual(type(r27.area()), int)
        r28 = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r28.area(), 4)
        self.assertEqual(type(r28.area()), int)
        with self.assertRaises(TypeError):
            r28.area(5)

    def test_display(self):
        """Public method to check area method"""
        r29 = Rectangle(2, 2)
        display_example = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r29.display()
        self.assertEqual(fakeOutput.getvalue(), display_example)
        r30 = Rectangle(2, 3, 2, 2)
        display_example = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r30.display()
        self.assertEqual(fakeOutput.getvalue(), display_example)

    def test_str(self):
        """Public method to check __str__ method return"""
        r31 = Rectangle(4, 6, 2, 1, 12)
        display_example = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r31)
        self.assertEqual(fakeOutput.getvalue(), display_example)

    def test_update(self):
        """Public method to check update method"""
        r32 = Rectangle(10, 10, 10, 10)
        r32.update(89)
        display_example = "[Rectangle] (89) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r32)
        self.assertEqual(fakeOutput.getvalue(), display_example)
        r32.update(89, 2)
        display_example = "[Rectangle] (89) 10/10 - 2/10\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r32)
        self.assertEqual(fakeOutput.getvalue(), display_example)
        r32.update(89, 2, 3)
        display_example = "[Rectangle] (89) 10/10 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r32)
        self.assertEqual(fakeOutput.getvalue(), display_example)
        r32.update(89, 2, 3, 4)
        display_example = "[Rectangle] (89) 4/10 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r32)
        self.assertEqual(fakeOutput.getvalue(), display_example)
        r32.update(89, 2, 3, 4, 5)
        display_example = "[Rectangle] (89) 4/5 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r32)
        self.assertEqual(fakeOutput.getvalue(), display_example)
        with self.assertRaises(TypeError):
            r32.update()
        with self.assertRaises(ValueError):
            r32.update(2, 2, -2, 2, 2)
        with self.assertRaises(ValueError):
            r32.update(2, -2, 2, 2, 2)
        with self.assertRaises(ValueError):
            r32.update(2, 0, 2, 2, 2)
        with self.assertRaises(ValueError):
            r32.update(2, 2, 0, 2, 2)
        with self.assertRaises(ValueError):
            r32.update(2, 2, 2, -1, 0)
        with self.assertRaises(ValueError):
            r32.update(2, 2, 2, 0, -1)
        with self.assertRaises(TypeError):
            r32.update(2, None)
        with self.assertRaises(TypeError):
            r32.update(3, 3, 3, 3, 3, 3, 3)
        with self.assertRaises(TypeError):
            r32.update(2, (3 + 5j), 8)
        with self.assertRaises(TypeError):
            r32.update(2, 5, [8, 7])
        with self.assertRaises(TypeError):
            r32.update(2, 5.2, 6)
        with self.assertRaises(TypeError):
            r32.update(2, {'malo': 3, 'bueno': 6}, 6)
        with self.assertRaises(TypeError):
            r32.update(2, True, 6)
        with self.assertRaises(TypeError):
            r32.update(2, (4, 3), 6)
        with self.assertRaises(TypeError):
            r32.update(2, "sY CiRbo", 6)
        with self.assertRaises(TypeError):
            r32.update(2, ([4, 3]), 6)
        with self.assertRaises(TypeError):
            r12 = Rectangle(2, 8, (3 + 5j))
        with self.assertRaises(TypeError):
            r32.update(2, [8, 7], 5)
        with self.assertRaises(TypeError):
            r32.update(2, 5, 5.2)
        with self.assertRaises(TypeError):
            r32.update(2, 6, {'malo': 3, 'bueno': 6})
        with self.assertRaises(TypeError):
            r32.update(2, 6, True)
        with self.assertRaises(TypeError):
            r32.update(2, 6, (4, 3))
        with self.assertRaises(TypeError):
            r32.update(2, 6, "sY CiRbo")
        with self.assertRaises(TypeError):
            r32.update(2, 6, ([4, 3]))
        with self.assertRaises(TypeError):
            r32.update(2, 8, 5, (3 + 5j))
        with self.assertRaises(TypeError):
            r32.update(2, 5, 5, [8, 7])
        with self.assertRaises(TypeError):
            r32.update(2, 5, 5, 5.2)
        with self.assertRaises(TypeError):
            r32.update(2, 6, 4, {'malo': 3, 'bueno': 6})
        with self.assertRaises(TypeError):
            r32.update(2, 6, 4, True)
        with self.assertRaises(TypeError):
            r32.update(2, 6, 3, (4, 3))
        with self.assertRaises(TypeError):
            r26 = Rectangle(2, 6, 5, "sY CiRbo")
        with self.assertRaises(TypeError):
            r32.update(2, 6, 9, ([4, 3]))
        with self.assertRaises(TypeError):
            r32.update(2, 8, 5, 4, (3 + 5j))
        with self.assertRaises(TypeError):
            r32.update(2, 5, 5, 3, [8, 7])
        with self.assertRaises(TypeError):
            r32.update(2, 5, 5, 4, 5.2)
        with self.assertRaises(TypeError):
            r32.update(2, 6, 4, 2, {'malo': 3, 'bueno': 6})
        with self.assertRaises(TypeError):
            r32.update(2, 6, 4, 5, True)
        with self.assertRaises(TypeError):
            r32.update(2, 6, 3, 9, (4, 3))
        with self.assertRaises(TypeError):
            r32.update(2, 6, 5, 6, "sY CiRbo")
        with self.assertRaises(TypeError):
            r32.update(2, 6, 9, 7, ([4, 3]))
