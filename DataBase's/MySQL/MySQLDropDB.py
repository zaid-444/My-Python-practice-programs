# How to remove DataBase

import mysql.connector

try:
    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "zaid0444"
    )
    cur = con.cursor()

    cur.execute("drop database test1")

    print("DataBase Deleted")
except mysql.connector.DatabaseError as db:
    print(db)