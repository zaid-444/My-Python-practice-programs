# Write a python program which will update employee salary based on employee number

import oracledb as orcc

def updateemp():
    try:
        con = orcc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()
        
        cur.execute("update employee set sal=3.4 where eno=100")
        con.commit()
        print("Record Updated")
    except orcc.DatabaseError as db:
        print(db)

updateemp()