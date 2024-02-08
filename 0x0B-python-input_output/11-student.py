#!/usr/bin/python3
""" Student class module
"""


class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        """ Initializes a Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation
        of a Student instance

        Args:
            attrs (list, optional): List of attributs
            to include in the dictionary.
            Defaults to None, in which case all attributes are included.

        Returns:
            dict: Dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student
        instance from a dictionary

        Args:
            json (dict): Dictionary containing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
