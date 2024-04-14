#!/usr/bin/python3
"""
Script to change the name of a State object 
with id = 2 to "New Mexico"
in the database hbtn_0e_6_usa
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

    # Get the state with id = 2
    state = session.query(State).filter_by(id=2).first()

    # Change the name of the state to "New Mexico"
    state.name = "New Mexico"

    # Commit the change
    session.commit()

    # Close the session
    session.close()

