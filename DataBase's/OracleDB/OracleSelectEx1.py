# Write a python program which will read the records from employee table

import oracledb as orc

def selectrecord():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()

        cur.execute("select * from employee")

        while True:
            record = cur.fetchone()
            if record != None:
                print(record)
            else:
                break

    except orc.DatabaseError as db:
        print(db)

selectrecord()