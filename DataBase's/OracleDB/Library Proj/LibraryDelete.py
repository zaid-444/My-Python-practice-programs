import oracledb as orc

def deletebook():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()

        bno = int(input("Enter Book no. To Delete: "))
        cur.execute("delete from library where bno = %d" %bno)
        con.commit()
        if cur.rowcount:
            print("Book Deleted...")
        else:
            print("Book Does not exist")
    except orc.DatabaseError as db:
        print(db)
    except ValueError:
        print("Enter Book no. not alphabates")