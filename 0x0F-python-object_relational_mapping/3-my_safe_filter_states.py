#!/usr/bin/python3
"""Script that takes in an argument,
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, using parameterized queries."""

if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    param = (argv[4], )

    c.execute("SELECT * FROM states WHERE name = %s\
            ORDER BY states.id ASC", param)

    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
