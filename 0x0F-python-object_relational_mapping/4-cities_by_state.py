#!/usr/bin/python3
"""
Lists all cities from the database.
Requires three arguments: mysql username, mysql password, database name.
Connects to default host (localhost) and port (3306).
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb as mysql

    # Connect to the database
    db = mysql.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    # Execute SQL query to retrieve cities with their states
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
             ORDER BY cities.id ASC")
    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
