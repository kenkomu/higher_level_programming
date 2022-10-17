#!/usr/bin/python3
import MySQLdb
conn = MySQLdb.connect(host="localhost", port=3306,
                       user="root", passwd="root", db="my_db")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
