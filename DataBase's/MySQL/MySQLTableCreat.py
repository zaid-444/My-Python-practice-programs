# How to create table in mysql

import mysql.connector

def createtable():
    try:
        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "zaid0444",
            database = "test1"
        )
        cur = con.cursor()

        cq = "create table employee(eno int primary key,name varchar(20) not null, sal decimal(8,2), compname varchar(10))"

        cur.execute(cq)
        print("Table Created Successfully")
    except mysql.connector.DatabaseError as db:
        print(db)

createtable()