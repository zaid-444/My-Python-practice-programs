# Write a python program which will read employee values from keyboard and insert as a record in employee table

import oracledb as orc

def insertrecord():
    try:
        con = orc.connect("system/tiger@localhost/orcl") # orcl is service id
        cur = con.cursor()
        iq = "insert into employee values(10,'Zaid',3.2,'Mumbai')"
        cur.execute(iq)
        con.commit()
        print("Record Added")
    except orc.DatabaseError as db:
        print("DataBase Error=>",db)

insertrecord()