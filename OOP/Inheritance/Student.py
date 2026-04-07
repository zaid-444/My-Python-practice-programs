from College import College
import mysql.connector

class Student(College):
    def getStudDet(self):
        self.sno = int(input("Enter Student Roll No.: "))
        self.sname = input("Enter Student Name: ")
        self.sbranch = input("Enter Student Branch: ")
        self.getColDet()
        self.getUnivDet()
    
    def saveToMySQL(self):
        try:
            con = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "zaid0444",
                database = 'venom1'
            )
            cur = con.cursor()

            iq = "insert into univ values(%d,'%s','%s','%s','%s','%s','%s')"
            cur.execute(iq %(self.sno,self.sname,self.sbranch,self.cname,self.cloc,self.uname,self.uloc))
            con.commit()

            print("="*50)
            print("{}'s Information Added to Database Successfully...".format(self.sname))

        except mysql.connector.DatabaseError as db:
            print(db)