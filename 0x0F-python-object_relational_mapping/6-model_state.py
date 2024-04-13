#!/usr/bin/python3
"""
Script to link a class to a database table
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Retrieve database connection details from command-line arguments
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create the database URL
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pwd, db_name)

    # Create an engine to manage the database connection
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create the tables in the database based on the class definitions
    Base.metadata.create_all(engine)
