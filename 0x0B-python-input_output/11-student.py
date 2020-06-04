#!/usr/bin/python3
"""This file containt a class named Student"""


class Student:
    """Class student"""

    def __init__(self, first_name, last_name, age):
        """Special method to init intances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function that returns the dictionary description with simple data
        structure"""
        return self.__dict__
