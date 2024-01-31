#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    """
    Prints a square composed of the character '#' with the specified size.

    Args:
        size (int): The length of the sides of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        print("x" * size)
