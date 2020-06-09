#!/usr/bin/python3
"""Unittest for Base class from almost circle python project
"""
import unittest
from models.base import Base


class Test_base(unittest.TestCase):
    """Class test using unittest"""
    def test_Base(self):
        """Test constructor"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        with self.assertRaises(TypeError):
            b2 = Base(2, 2)
