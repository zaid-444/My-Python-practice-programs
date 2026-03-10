import oracledb as orc

def viewallbooks():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()

        cur.execute("select * from library")
        colname = cur.description
        records = cur.fetchall()

        if not records:
            print("No Books Found")
        else:
            print("="*40)
            for col in colname:
                print(col[0],end="\t")
            print()

            print("-"*40)
            for record in records:
                for val in record:
                    print(val,end="\t")
                print()
            print("="*40)
    except orc.DatabaseError as db:
        print(db)

def viewbook():pass