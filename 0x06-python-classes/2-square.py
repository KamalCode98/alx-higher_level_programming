#!/usr/bin/python3
"""
A Square class that defines a square
"""


class Square:
    """Square with size"""

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
