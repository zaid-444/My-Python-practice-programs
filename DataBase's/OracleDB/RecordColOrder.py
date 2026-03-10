import oracledb as orc

def selectcolrecord():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()

        cur.execute("select * from %s order by eno" %input("Enter table name: "))

        columns = cur.description
        for column in columns:
            print(column[0],end="\t")
        print()

        records = cur.fetchall()
        for record in records:
            for val in record:
                print(val,end="\t")
            print()
    except orc.DatabaseError as db:
        print("Error in Database: ",db)