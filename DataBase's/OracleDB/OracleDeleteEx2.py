# Write a python program which will delete the record based on Employee number.

import oracledb

def deleterecord():
    try:
        con = oracledb.connect("system/tiger@localhost/orcl")
        cur = con.cursor()
        empno = int(input("Enter Employee Number: "))
        cur.execute("delete from employee where eno=%d" %empno)
        con.commit()
        if cur.rowcount:
            print("{} Record Deleted".format(cur.rowcount))
        else:
            print("{} Record Does not Exist".format(empno))
    except oracledb.DatabaseError as db:
        print(db)

deleterecord()