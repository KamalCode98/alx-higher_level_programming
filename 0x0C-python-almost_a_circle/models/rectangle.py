#!/usr/bin/python3
"""
module for Rectangle Class
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X coordinate of the rectangle's position.
                               Defaults to 0.
            y (int, optional): Y coordinate of the rectangle's position.
                               Defaults to 0.
            id (int, optional): ID value. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        self.__y = value
