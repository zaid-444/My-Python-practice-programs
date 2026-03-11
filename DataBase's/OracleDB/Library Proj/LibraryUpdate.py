import oracledb as orc

def updatebook():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()

        bno = int(input("Enter Book no. to Update book: "))
        bname = input("Enter Book Name: ")
        price = float(input("Enter Price of Book: "))
        pub = input("Enter Book Publication: ")

        cur.execute("update library set bname='%s', price=%f, pub='%s' where bno=%d" %(bname,price,pub,bno))
        con.commit()

        if cur.rowcount:
            print("Book Update Successfully")
        else:
            print("Book not Exist")

    except orc.DatabaseError as db:
        print(db)

    except ValueError:
        print("Please Enter Correct info.")