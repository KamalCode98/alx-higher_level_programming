#!/usr/bin/python3
"""
Script to print the State object with the name passed as an argument
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Get database connection details and
    state name from command-line arguments
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create the database URL
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(username,
                                                         password, database)

    # Create an engine to manage the database connection
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects with the given name
    state = session.query(State)\
        .filter(State.name == state_name)\
        .first()

    # Print the result or "Not found" if no state matches the name
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
