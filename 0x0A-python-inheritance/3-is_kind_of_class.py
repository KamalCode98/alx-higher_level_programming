#!/usr/bin/python3
"""
Module 3-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
