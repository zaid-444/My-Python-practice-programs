# Program for Creating DataBase
import mysql.connector

def createdatabase():
    try:
        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "zaid0444"
        )
        cur = con.cursor()

        cq = "create database test1"
        cur.execute(cq)
        print("DataBase Created Successfully...")

    except mysql.connector.Error as db:
        print(db)

createdatabase()