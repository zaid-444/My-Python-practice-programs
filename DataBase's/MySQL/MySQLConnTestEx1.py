# Program for How to get the Connection from MySql Database

import mysql.connector

try:
    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "zaid0444"
    )
    print("Successfully connected to DataBase")
except mysql.connector.Error as db:
    print(db)