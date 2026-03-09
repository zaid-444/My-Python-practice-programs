# Write a python program which will delete the record based on Employee number.

import oracledb as orc

def deleteemp():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()
        cur.execute("delete from employee where eno=101")
        con.commit()

        print("{} Record Deleted..".format(cur.rowcount))
    except orc.DatabaseError as db:
        print("Error :",db)

deleteemp()