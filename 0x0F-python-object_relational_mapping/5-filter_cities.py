#!/usr/bin/python3
"""
Script lists all cities of a given state from the database.
Requires three arguments: mysql username, mysql password, database name.
Connects to default host (localhost) and port (3306).
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb as mysql

    # Connect to the database
    database = mysql.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()

    # Use parameterized query to prevent SQL injection
    state_name = argv[4]
    cursor.execute("SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC", (state_name,))

    # Fetch the results
    rows = cursor.fetchall()

    # Extract city names
    cities = [row[0] for row in rows]

    # Print the city names
    print(', '.join(cities))

    # Close the cursor and database connection
    cursor.close()
    database.close()