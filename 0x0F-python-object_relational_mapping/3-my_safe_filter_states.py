#!/usr/bin/python3
"""
The script retrieves and displays a list of all cities
stored in the 'hbtn_0e_4_usa' database, with comments added.
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb as mysql

    # Connect to the database
    db_connection = mysql.connect(user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connection.cursor()

    # Sanitize the input argument
    sanitized_name = argv[4]

    # Execute the query
    db_cursor.execute("SELECT * FROM states WHERE name = %s\
            ORDER BY states.id ASC", (sanitized_name,))

    # Fetch and print the results
    result_set = db_cursor.fetchall()
    for row in result_set:
        print(row)

    # Close the cursor and database connection
    db_cursor.close()
    db_connection.close()
