# Write a python program which will change the col sizes of employee table

import oracledb

def altertable():
    try:
        con = oracledb.connect("system/tiger@localhost/orcl")
        cur = con.cursor()
        aq = "alter table employee modify(eno number(3), name varchar2(15))"
        cur.execute(aq)
        print("Table Modify Successfully")
    except oracledb.DatabaseError as err:
        print(err)

altertable()