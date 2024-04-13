#!/usr/bin/python3
"""
Script lists all State objects from a given database.
Requires three arguments: mysql username, mysql password, database name.
Connects to host localhost and default port (3306).
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    # Create a session
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)

    # Create tables if they do not exist
    Base.metadata.create_all(engine)

    # Query and print State objects
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))

    # Close the session
    session.close()