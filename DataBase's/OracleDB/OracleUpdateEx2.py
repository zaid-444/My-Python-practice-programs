import oracledb as orc

def updaterecord():
    while True:
        try:
            con = orc.connect("system/tiger@localhost/orcl")
            cur = con.cursor()

            eno = int(input("Enter Employee number to update salary: "))
            sal = float(input("Enter New Salary: "))

            cur.execute("update employee set sal=%f where eno=%d" %(sal,eno))
            con.commit()

            if cur.rowcount:
                print("Employee Updated")
            else:
                print("Employee Not Exist")

            print("-"*50)
            ch = input("Do u want to update another employee (yes/no): ")

            if ch.lower() == "no":
                print("Thanks for using this application")
                break
        except orc.DatabaseError as db:
            print(db)

        except ValueError:
            print("Enter correct employee number and salary")

updaterecord()