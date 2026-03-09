# Write a python program which will add a new col to the employee table 

import oracledb as orc

def addcol():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()
        aq = "alter table employee add (addr varchar2(30) not null)"
        cur.execute(aq)
        print("Col Added successfully")
    except orc.DatabaseError as db:
        print("DataBase Error=>",db)

addcol()