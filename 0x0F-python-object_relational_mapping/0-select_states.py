#!/usr/bin/python3
"""
Script that retrieves and prints all states from a database
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # Connect to the database
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()

    # Execute the query
    cursor.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    
    # Fetch the results
    rows = cursor.fetchall()

    # Print the states
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    database.close()
