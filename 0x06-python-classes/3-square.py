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
            param1 self: instance
            param2 int: size of the square

        Returns:
            - None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Public instance method that calculates the square area

        Args:
            param1 self: instance

        Returns:
            int: square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute

        Args:
            param1 self: instance

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute

        Args:
            param1 self: instance
            param2 value: new size value

        Returns:
            - None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
