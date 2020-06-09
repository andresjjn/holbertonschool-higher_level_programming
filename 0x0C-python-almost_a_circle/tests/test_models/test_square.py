  
#!/usr/bin/python3
"""Unittest for entire almost circle python project
"""
import unittest
import pep8
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class test_Square(unittest.TestCase):
    """Class testing for Square using unittest"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_types_constructor(self):
        """Public method to check types of data in constructor class method"""
        r = Square(10, 2)
        self.assertIsInstance(r, Square)
        with self.assertRaises(TypeError):
            r1 = Square(None)
        with self.assertRaises(TypeError):
            r2 = Square()
        with self.assertRaises(TypeError):
            r3 = Square(3, 3, 3, 3, 3, 3, 3)
        with self.assertRaises(TypeError):
            r4 = Square((3 + 5j))
        with self.assertRaises(TypeError):
            r5 = Square([8, 7])
        with self.assertRaises(TypeError):
            r6 = Square(5.2)
        with self.assertRaises(TypeError):
            r7 = Square({'malo': 3, 'bueno': 6})
        with self.assertRaises(TypeError):
            r8 = Square(True)
        with self.assertRaises(TypeError):
            r9 = Square((4, 3))
        with self.assertRaises(TypeError):
            r10 = Square("sY CiRbo")
        with self.assertRaises(TypeError):
            r11 = Square(([4, 3]))
        with self.assertRaises(TypeError):
            r12 = Square(8, (3 + 5j))
        with self.assertRaises(TypeError):
            r13 = Square(5, [8, 7])
        with self.assertRaises(TypeError):
            r14 = Square(5, 5.2)
        with self.assertRaises(TypeError):
            r15 = Square(6, {'malo': 3, 'bueno': 6})
        with self.assertRaises(TypeError):
            r16 = Square(6, True)
        with self.assertRaises(TypeError):
            r17 = Square(6, (4, 3))
        with self.assertRaises(TypeError):
            r18 = Square(6, "sY CiRbo")
        with self.assertRaises(TypeError):
            r19 = Square(6, ([4, 3]))
        with self.assertRaises(TypeError):
            r20 = Square(8, 5, (3 + 5j))
        with self.assertRaises(TypeError):
            r21 = Square(5, 5, [8, 7])
        with self.assertRaises(TypeError):
            r22 = Square(5, 5, 5.2)
        with self.assertRaises(TypeError):
            r23 = Square(6, 4, {'malo': 3, 'bueno': 6})
        with self.assertRaises(TypeError):
            r24 = Square(6, 4, True)
        with self.assertRaises(TypeError):
            r25 = Square(6, 3, (4, 3))
        with self.assertRaises(TypeError):
            r26 = Square(6, 5, "sY CiRbo")
        with self.assertRaises(TypeError):
            r27 = Square(6, 9, ([4, 3]))
        with self.assertRaises(TypeError):
            r27 = Square(6, 9, None)
        with self.assertRaises(TypeError):
            r27 = Square(6, None, 9)
        with self.assertRaises(TypeError):
            r27 = Square(None, 6, 9,)
