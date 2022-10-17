#!/usr/bin/python3
"""
    script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys


def main():
    """
        main - lists all states from the database hbtn_0e_0_usa
    """
    conn = MySQLdb.connect(
        user="root",
        passwd="root",
        db="hbtn_0e_0_usa"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
