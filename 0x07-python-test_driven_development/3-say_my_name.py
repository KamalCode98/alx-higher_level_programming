#!/usr/bin/python3
"""Module for say_my_name method."""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format: "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
