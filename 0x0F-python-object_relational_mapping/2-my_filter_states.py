#!/usr/bin/python3
"""
Script that retrieves and prints states from a database where the name matches
the provided argument.
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # Connect to the database
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()

    # Execute the query
    cursor.execute("""SELECT * FROM states WHERE name = '{}'\
            ORDER BY states.id ASC""".format(argv[4]))

    # Fetch the results
    rows = cursor.fetchall()

    # Print the matching states
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    # Close the cursor and database connection
    cursor.close()
    database.close()
