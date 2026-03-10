import oracledb as orc

def addbook():
    while True:
        try:
            con = orc.connect("system/tiger@localhost/orcl")
            cur = con.cursor()

            print("-"*50)
            bno = int(input("Enter Book Number: "))
            bname = input("Enter Book Name: ")
            bprice = float(input("Enter Book Price: "))
            bpub = input("Enter Book Publication: ")
            print("-"*50)

            iq = "insert into library values(%d,'%s',%f,'%s')"
            cur.execute(iq % (bno,bname,bprice,bpub))

            con.commit()

            print("{} Book Added".format(cur.rowcount))
            print("-"*50)

            ch = input("Do u want to Add another Book(yes/no): ")
            if ch.lower() == "no":
                break

        except orc.DatabaseError as db:
            print(db)

        except ValueError:
            print("Something entered wrong")