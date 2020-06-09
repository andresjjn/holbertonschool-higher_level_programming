#!/usr/bin/python3
"""This file contain a class named base"""
import json
import re
from inspect import getargspec


class Base:
    """Class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""

        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base. __nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """Instance method that writes the JSON string representation of list_objs
        to a file
        Args:
            list_objs = Objets list to write in a file"""
        l = []
        if list_objs is not None:
            for a in list_objs:
                l.append(a.to_dictionary())
        with open("%s.json" % cls.__name__, mode='w') as f:
            f.write(Base.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """Instance method that returns the list of the JSON string representation
        json_string
        Args:
            json_string is a string representing a list of dictionaries"""
        b = []
        if json_string is None or json_string == "":
            return b
        a = re.findall("{.*?}", json_string)
        for i in a:
            b.append(json.loads(i))
        return b

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        Args:
            list of dictionaries
        Return:
            JSON string representation of any position of list"""
        if not list_dictionaries:
            return "[]"
        for i in range(len(list_dictionaries)):
            if type(list_dictionaries[i]) is not dict:
                raise TypeError("The list not contain dictionaries")
        a = "["
        for b in range(len(list_dictionaries)):
            if b < i:
                a = a + json.dumps(list_dictionaries[b]) + ", "
            else:
                a = a + json.dumps(list_dictionaries[b])
        a = a + "]"
        return a

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with all attributes already set
        Args:
            Dictionary with instance to new class
        Return:
            New instance class
        """
        if cls.__name__ == "Rectangle":
            a = cls(1, 1, 1, 1, 1)
            a.update(
                id=dictionary["id"], width=dictionary["width"],
                height=dictionary["height"], x=dictionary["x"],
                y=dictionary["y"])
            return a
        elif cls.__name__ == "Square":
            b = cls(1, 1, 1, 1)
            b.update(
                id=dictionary["id"], size=dictionary["size"],
                x=dictionary["x"], y=dictionary["y"])
            return b
        else:
            return None

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances
        Args:
            Class"""
        try:
            with open(
                    "%s.json" % cls.__name__, mode='r', encoding="utf-8") as f:
                a = f.read()
        except:
            a = []
            return a
        b = cls.from_json_string(a)
        c = []
        for i in b:
            d = json.loads(i)
            c.append(cls.create(**d))
        return c
