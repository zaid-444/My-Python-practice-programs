import mysql.connector
class Employee:
    def getempdata(self):
        self.eno = int(input("Enter Employee Number: "))
        self.ename = input("Enter Employee Name: ")
        self.sal = float(input("Enter Employee Salary: "))

    def saveemp(self):
        while True:
            try:
                con = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    passwd = "zaid0444",
                    database = "venom1"
                )
                cur = con.cursor()

                print("-"*50)
                self.getempdata()

                iq = "insert into employee values(%d,'%s',%f)"
                cur.execute(iq %(self.eno,self.ename,self.sal))
                con.commit()

                print("-"*50)
                print("Employee Added Successfully")
                print("-"*50)

                ch = input("Do u Want to add another employee(yes/no): ")
                if ch.lower() == "no":
                    print("Thanks for using this program")
                    break

            except mysql.connector.DatabaseError as db:
                print(db)

e = Employee()

e.saveemp()