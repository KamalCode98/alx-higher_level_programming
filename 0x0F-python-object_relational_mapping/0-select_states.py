#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

def connect_to_database(host, port, user, password, database):
    """Connects to a MySQL database and returns the connection object."""
    return MySQLdb.connect(host=host, port=port, user=user, passwd=password, db=database)

def execute_query(connection, query):
    """Executes a SQL query on the given database connection and returns the result."""
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def print_results(results):
    """Prints the results of a query."""
    for row in results:
        print(row)

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    host = "localhost"
    port = 3306
    user = argv[1]
    password = argv[2]
    database = argv[3]

    try:
        db = connect_to_database(host, port, user, password, database)
        results = execute_query(db, "SELECT * FROM states")
        print_results(results)
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))
        exit(1)