# Program for Obtaining Column Names

import oracledb as orc

def selectcol():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()

        cur.execute("select * from employee")

        col = cur.description
        for c in col:
            print(c[0],end="\t")
        print()

    except orc.DatabaseError as db:
        print(db)

selectcol()