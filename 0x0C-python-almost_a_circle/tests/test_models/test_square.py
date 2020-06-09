  
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
            r32 = Square(6, 5, "sY CiRbo")
        with self.assertRaises(TypeError):
            r33 = Square(6, 9, ([4, 3]))
        with self.assertRaises(TypeError):
            r34 = Square(6, 9, None)
        with self.assertRaises(TypeError):
            r35 = Square(6, None, 9)
        with self.assertRaises(TypeError):
            r36 = Square(None, 6, 9,)

    def test_str(self):
        """Public method to check __str__ method return"""
        r28 = Square(5)
        display_example = "[Square] (2) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r28)
        self.assertEqual(fakeOutput.getvalue(), display_example)
        r29 = Square(2, 2)
        display_example = "[Square] (3) 2/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r29)
        self.assertEqual(fakeOutput.getvalue(), display_example)
        r30 = Square(3, 1, 3)
        display_example = "[Square] (4) 1/3 - 3\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r30)
        self.assertEqual(fakeOutput.getvalue(), display_example)

    def test_update(self):
        """Public method to check update method"""
        r32 = Square(5)
        r32.update(10)
        display_example = "[Square] (10) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r32)
        self.assertEqual(fakeOutput.getvalue(), display_example)
        r32.update(1, 2)
        display_example = "[Square] (1) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r32)
        self.assertEqual(fakeOutput.getvalue(), display_example)
        r32.update(1, 2, 3)
        display_example = "[Square] (1) 3/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r32)
        self.assertEqual(fakeOutput.getvalue(), display_example)
        r32.update(1, 2, 3, 4)
        display_example = "[Square] (1) 3/4 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r32)
        self.assertEqual(fakeOutput.getvalue(), display_example)
        with self.assertRaises(ValueError):
            r32.update(2, -2, 2, 2)
        with self.assertRaises(ValueError):
            r32.update(0, 0, 2, 2)
        with self.assertRaises(ValueError):
            r32.update(2, 2, -1, 0)
        with self.assertRaises(ValueError):
            r32.update(2, 2, 0, -1)
        with self.assertRaises(TypeError):
            r32.update(2, None)
        with self.assertRaises(TypeError):
            r32.update(3, 3, 3, 3, 3, 3, 3)
        with self.assertRaises(TypeError):
            r32.update(2, (3 + 5j))
        with self.assertRaises(TypeError):
            r32.update(2, [8, 7])
        with self.assertRaises(TypeError):
            r32.update(2, 5.2)
        with self.assertRaises(TypeError):
            r32.update(2, {'malo': 3, 'bueno': 6}, 6)
        with self.assertRaises(TypeError):
            r32.update(2, True)
        with self.assertRaises(TypeError):
            r32.update(2, (4, 3))
        with self.assertRaises(TypeError):
            r32.update(2, "sY CiRbo")
        with self.assertRaises(TypeError):
            r32.update(2, ([4, 3]))
        with self.assertRaises(TypeError):
            r32.update(2, 8, (3 + 5j))
        with self.assertRaises(TypeError):
            r32.update(2, 5, [8, 7])
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
            r32.update(2, 6, 5, "sY CiRbo")
        with self.assertRaises(TypeError):
            r32.update(2, 6, 9, ([4, 3]))


    def test_setters(self):
        """Public method to check types and values de getters methods"""
        r26 = Square(2)
        r26.size = 8
        self.assertEqual(r26.size, 8)
        self.assertEqual(type(r26.size), int)
        with self.assertRaises(TypeError):
            r26.size = (3 + 5j)
        with self.assertRaises(TypeError):
            r26.size = [5, 7]
        with self.assertRaises(TypeError):
            r26.size = 5.2
        with self.assertRaises(TypeError):
            r26.size = {'malo': 3, 'bueno': 6}
        with self.assertRaises(TypeError):
            r26.size = True
        with self.assertRaises(TypeError):
            r26.size = (5, 8)
        with self.assertRaises(TypeError):
            r26.size = "sY CiRbo"
        with self.assertRaises(TypeError):
            r26.size = ([4, 3])
        with self.assertRaises(ValueError):
            r26.size = (0)
        with self.assertRaises(ValueError):
            r26.size = (-1)

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

        def test_to_dictionary(self):
            """Public method to check if return a dictionary"""
            r40 = Square(10, 2, 1)
            r40_dictionary = r40.to_dictionary()
            r40_dictionary_test = {'id': 4, 'x': 2, 'size': 10, 'y': 1}
            self.assertDictEqual(r40_dictionary, r40_dictionary_test)
            self.assertEqual(type(r40_dictionary), dict)

            r41 = Square(1, 1)
            r41.update(**r40_dictionary)
            self.assertNotEqual(r40, r41)


if __name__ == '__main__':
    unittest.main()