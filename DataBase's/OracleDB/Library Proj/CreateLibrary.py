# Write a python program which will implement the following project
# ========================================
    # Library Management System
# ========================================
    # 1. Add a New Book
    # 2. Delete a Book
    # 3. Update Book Details
    # 4. View Book Details
    # 5. View All Book Details
    # 6. Exit
# ========================================
    # Enter Ur Choice:
# ========================================

import oracledb as orc

try:
    con = orc.connect("system/tiger@localhost/orcl")
    cur = con.cursor()

    cq = "create table library(bno number(3) primary key, bname varchar2(20) not null, price number(4,2) not null, pub varchar(20) not null)"

    cur.execute(cq)

    print("Table Created Successfully")
except orc.DatabaseError as db:
    print("Error: ",db)