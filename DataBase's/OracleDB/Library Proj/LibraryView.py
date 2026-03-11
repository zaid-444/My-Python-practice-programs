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

def viewbook():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()

        bno = int(input("Enter Book No. to View: "))
        cur.execute("select * from library where bno = %d" %bno)

        record = cur.fetchone()
        if not record:
            print("Book Not Found")
        else:
            print("-"*50)
            print("Book Number :     {}".format(record[0]))
            print("Book Name :       {}".format(record[1]))
            print("Book Price :      {}".format(record[2]))
            print("Book Publication :{}".format(record[3]))
            print("-"*50)
    except orc.DatabaseError as db:
        print(db)
    except ValueError:
        print("Book Number is Wrong..")