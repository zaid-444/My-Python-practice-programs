# Write a python program which will update employee company name and employee salary based on emp no.

import mysql.connector

def updateemp():
    try:
        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "zaid0444",
            database = "test1"
        )
        cur = con.cursor()

        print("-"*50)
        eno = int(input("Enter Employee no. to updated CompName and Sal: "))
        ecomp = input("Enter New Company Name: ")
        esal = float(input("Enter New Salary: "))
        print("-"*50)

        cur.execute("update employee set compname=%s,sal=%s where eno=%s",(ecomp,esal,eno))
        con.commit()
        
        if cur.rowcount:
             print("Employee Updated")
        else:
             print("Employee Does not Exist")
    except mysql.connector.DatabaseError as db:
        print(db)

updateemp()