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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        b = dict()
        if not attrs:
            return self.__dict__
        elif type(attrs) == list:
            for i in attrs:
                for an in sorted(self.__dict__):
                    if i == an:
                        b.update({i: self.__dict__[i]})
        return b
        
    def reload_from_json(self, json):
        """Method to replaces all attributes of the Student instance"""
        for i in json:
            self.__dict__.update({i: json[i]})
