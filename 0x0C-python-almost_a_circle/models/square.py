#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class, inherits from Rectangle.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize a Square instance.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Return string representation of the Square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Getter for the size attribute.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for the size attribute.'''
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method to update instance attributes.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Update instance attributes using *args and **kwargs.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Return dictionary representation of the Square instance.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
