# Program for deleting table

import oracledb as orc

def removetable():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()
        cq = "drop table employee"
        cur.execute(cq)
        print("Table Deleted Successfully")
    except orc.DatabaseError as dbe:
        print(dbe)