# Write a python program which will create employee table with Suitable col names

import oracledb as orc
try:
    con = orc.connect("system/tiger@localhost/orcl")
    cur = con.cursor()

    cq = "create table employee(eno number(2) primary key, name varchar(10) not null, marks number(5,2) not null)"

    cur.execute(cq)

    print("Table Created Successfully")
except orc.DatabaseError as db:
    print(db)