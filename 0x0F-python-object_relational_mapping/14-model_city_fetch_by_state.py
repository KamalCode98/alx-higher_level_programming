#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
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

    # Query all cities and print them sorted by id
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state = session.query(State)\
               .filter(State.id == city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
