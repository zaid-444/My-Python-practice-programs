# Write a python program which will select the records of employee table 

import mysql.connector

def selectrecord():
    try:
        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "zaid0444",
            database = "test1"
        )
        cur = con.cursor()
        
        cur.execute("select * from employee")

        col = cur.description
        records = cur.fetchall()

        if records:
            print("="*50)
            for val in col:
                print(val[0],end="\t")
            print()
            print("="*50)
            for record in records:
                for val in record:
                    print(val,end="\t")
                print()
            print("="*50)
        else:
            print("No Data Available Currently")

    except mysql.connector.DatabaseError as db:
        print(db)

selectrecord()