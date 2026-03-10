import oracledb as orc

def selectrecordcol():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()

        cur.execute("select * from %s" %input("Enter Table Name: "))

        col = cur.description
        for c in col:
            print(c[0],end="\t")
        print()
        records = cur.fetchall()
        for record in records:
            for val in record:
                print("\t{}".format(val),end="\t")
            print()
    except orc.DatabaseError as db:
        print(db)

selectrecordcol()