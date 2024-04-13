#!/usr/bin/python3
"""File contains class State and instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class that inherits from base """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
