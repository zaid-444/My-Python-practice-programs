class Student:
    @classmethod
    def clgdet(cls):
        cls.cname = "R.B.Attal"
        cls.city = "Georai"

    def readstudvalues(self):
        self.sno = int(input("Enter Roll No.: "))
        self.name = input("Enter Student Name: ")
        self.marks = float(input("Enter Student Marks: "))

    def printstud(self):
        self.readstudvalues()
        print("="*50)
        self.clgdet()
        print("Roll No:",self.sno)
        print("Name:",self.name)
        print("Marks:",self.marks)
        print("Collage:",self.cname)
        print("City:",self.city)

s1 = Student()
s1.printstud()
print("="*50)
s2 = Student()
s2.printstud()