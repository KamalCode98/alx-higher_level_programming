#!/usr/bin/python3
"""
Class Square that defines a square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
"""


class Square:
    def __init__(self, size=0) -> None:
        """
        Constructor function

        Args:
        param1 (self): instance
        param2 (int): size of the square

        Returns:
        - None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
