#!/usr/bin/python3
"""
Script to list State objects containing the letter 'a'
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get database connection details from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Query State objects where the name contains the letter 'a'
    states_with_a = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()

    # Print the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
