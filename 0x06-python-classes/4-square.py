#!/usr/bin/python3
"""
A Square class that defines a square
"""


class Square:
    """Square with size"""
    def __init__(self, size=0):
        """
        Constructor function

        Args:
        par1 self: instance
        par2 int: size of the square

        Returns:
        - None
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method that calculates the square

        Args:
            par1 self: refer to instance

        Returns:
            int: square area
        """
        return self.__size ** 2
