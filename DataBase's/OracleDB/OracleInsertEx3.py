# Write a python program which will read employee values from keyboard and insert as a record in employee table

import oracledb as ordb

def insertrecord():
    while True:
        try:
            con = ordb.connect("system/tiger@localhost/orcl")
            cur = con.cursor()

            eno = int(input("Enter Employee Number: "))
            ename = input("Enter Employee Name: ")
            esal = float(input("Enter Employee Sal: "))
            eaddr = input("Enter Employee Address: ")

            iq = "insert into employee values (%d,'%s',%f,'%s')" %(eno,ename,esal,eaddr)

            cur.execute(iq)
            con.commit()
            print("Employee Added")
            
            ch = input("Do u want to add another Employee: ")
            if ch.lower() == "no":
                print("Thnxx....")
                break
        except ordb.DatabaseError as db:
            print("DataBase Error=>",db)
        except ValueError:
            print("Don't Enter empno and salary as Non-Int")
        

insertrecord()