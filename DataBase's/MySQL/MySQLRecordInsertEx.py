# Write a python program which will insert employee records in employee table of mysql by reading employee values from keyboard

import mysql.connector

def addemp():
    while True:
        try:
            con = mysql.connector.connect(
                host = "localhost",
                user = "root",
                passwd = "zaid0444",
                database = "test1"
            )
            cur = con.cursor()

            print("-"*50)
            empno = int(input("Enter Employee Number: "))
            ename = input("Enter Employee Name: ")
            esal = float(input("Enter Employee Salary: "))
            ecomp = input("Enter Employee Company: ")
            print("-"*50)

            cur.execute("insert into employee values(%d,'%s',%f,'%s')" %(empno,ename,esal,ecomp))
            con.commit()

            print("Employee Details Added")
            print("-"*50)
            while True:
                ch = input("Do U Want to Add Another Employee(yes/no): ")
                if ch.lower() in ("yes","no"):
                    break
                else:
                    print("Please Enter Yes or No")
            if ch.lower() == "no":
                break
        except mysql.connector.DatabaseError as db:
            print(db)

addemp()