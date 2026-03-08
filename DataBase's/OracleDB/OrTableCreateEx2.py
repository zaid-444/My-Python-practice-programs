# Write a python program which will create employee table with Suitable col names dynamically

import oracledb as orc
try:
    con = orc.connect("system/tiger@localhost/orcl")
    cur = con.cursor()

    cq = input("Enter Query to create table: ")
    cur.execute(cq)

    print("Table Created Successfully")
except orc.DatabaseError as db:
    print(db)