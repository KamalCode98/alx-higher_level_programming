#!/usr/bin/python3
"""
The script retrieves and displays a list of all cities
stored in the 'hbtn_0e_4_usa' database, with modified variable names.
"""

if __name__ == "__main__":

    from sys import argv
    import MySQLdb as mysql

    database = mysql.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")
    result_set = cursor.fetchall()

    for row in result_set:
        print(row)

    cursor.close()
    database.close()
