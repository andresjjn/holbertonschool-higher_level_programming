#!/usr/bin/python3
"""Unittest for Base class from almost circle python project
"""
import unittest
import pep8
from models.base import Base


class Test_base(unittest.TestCase):
    """Class test using unittest"""
    
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_Base(self):
        """Test constructor"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        with self.assertRaises(TypeError):
            b2 = Base(2, 2)

if __name__ == '__main__':
    unittest.main()