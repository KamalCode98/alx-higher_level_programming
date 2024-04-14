#!/usr/bin/python3
"""Contains the class definition of a City."""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City class inherits from Base
        Links to MySQL table 'cities'

        Attributes:
        id: column of auto-generated unique integer,
            can't be NULL, primary key
        name: column of string of 128 characters, can't be NULL
        state_id: column of integer, can't be NULL,
                  foreign key to states.id
        """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
