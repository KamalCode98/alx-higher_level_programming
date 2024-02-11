#!/usr/bin/python3
"""
module for base class
"""


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance.

        Args:
            id (int, optional): ID value.
                                If provided, set as the instance id.
                                Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
