#!/usr/bin/python3
"""Module for the add_integer function."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: The first integer.
        b: The second integer, default is 98.

    Raises:
        TypeError: If 'a' or 'b' are not integers or floats.

    Returns:
        The sum of the two integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
