# Write a python program which will delete a record from employee table based on employee number

import mysql.connector

def deleterec():
    try:
        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "zaid0444",
            database = "test1"
        )
        cur = con.cursor()

        print("-"*50)
        empno = int(input("Enter Employee Number to Delete: "))
        print("-"*50)

        cur.execute("delete from employee where eno=%d" %empno)
        con.commit()

        if cur.rowcount:
            print("Employee Deleted Successfully")
        else:
            print("Employee Does Not Exist")
    except mysql.connector.Error as db:
        print(db)

deleterec()