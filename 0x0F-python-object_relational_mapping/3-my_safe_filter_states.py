#!/usr/bin/python3
"""
The script retrieves and displays a list of all cities
stored in the 'hbtn_0e_4_usa' database, with comments added.
"""

if __name__ == "__main__":

    from sys import argv
    import MySQLdb as mysql

    # Connect to the database
    database = mysql.connect(user=argv[1], passwd=argv[2], db=argv[3])
    
    # Create a cursor object to execute SQL queries
    cursor = database.cursor()

    # Execute a SQL query to retrieve cities and their corresponding states
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")
    
    # Fetch all the rows from the result set
    result_set = cursor.fetchall()

    # Print the retrieved rows
    for row in result_set:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    database.close()
