#!/usr/bin/python3
"""
Script to delete all State objects with a name containing the letter 'a'
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
    # Query and delete all states with a name containing the letter 'a'
    states_to_delete = session.query(State)
    .filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()
    # Close the session
    session.close()
