#!/usr/bin/python3

"""
class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """square with size"""
    def __init__(self, size) -> None:
        """
        Constructor function

        Args:
        par1 self: instance
        par2 int: size of the square

        Returns:
        - None
        """
        self.__size = size
