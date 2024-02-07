#!/usr/bin/python3
"""collected module"""
class Student:
    """strudent class"""
    def __init__(self, first_name, last_name, age):
        """Initializetion of the student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """return a dictionary representation of a student"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.item():
            if key in attrs:
                my_dict[key] = value
        return my_dict
    def reload_from_json(self, json):
        """this function replace all attrebutes"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
