#!/usr/bin/python3
"""This file contain a class named base"""
import json


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
        if json_string == None or json_string == "":
            return "[]"
        a = json_string.split("}")
        for k in a.items():
            print(k)

        
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        Args:
            list of dictionaries
        Return:
            JSON string representation of any position of list"""
        if not list_dictionaries:
             return "[]"
        a = "["
        for b in range(len(list_dictionaries)):
            a = a + json.dumps(list_dictionaries[b])
        a = a + "]"
        return a
