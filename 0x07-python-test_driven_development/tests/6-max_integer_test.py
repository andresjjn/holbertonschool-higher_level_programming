#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_results(self):
        """Method to test results of module"""
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([-1, -30, 83, 47]), 83)
        self.assertAlmostEqual(max_integer([1, 2, 4]), 4)
        self.assertAlmostEqual(max_integer([3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, -2, -3, 4]), 4)
        self.assertAlmostEqual(max_integer([4]), 4)
        self.assertAlmostEqual(max_integer([1, 0, 0, 0]), 1)
        self.assertAlmostEqual(max_integer([-8]), -8)

    def test_types(self):
        """Method to test types input to module"""
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, 8)
        self.assertRaises(TypeError, max_integer, 8.999)
        self.assertRaises(TypeError, max_integer, str)
