# Write a python program which will implement the following Problem let us asume there exist a university which contain university name and location. Accept and display university details let us asume there exist a college which contains college name and it's location accept and display college details along with university details let us asume there exist a college in which there exist Student number, name and branch accept and display student details along with college and university details

class Univ:
    def getUnivDet(self):
        self.uname = input("Enter University Name: ")
        self.uloc = input("Enter University Location: ")
    def dispUniDet(self):
        print("-"*50)
        print("\tUniversity Name: {}".format(self.uname))
        print("\tUniversity Location: {}".format(self.uloc))

class College(Univ):
    def getColDet(self):
        self.cname = input("Enter College Name: ")
        self.cloc = input("Enter College Location: ")
    def dispColDet(self):
        print("-"*50)
        print("\tCollege Name :",self.cname)
        print("\tCollege Location :",self.cloc)

class Student(College):
    def getStudDet(self):
        self.sno = int(input("Enter Student Roll No.: "))
        self.sname = input("Enter Student Name: ")
        self.sbranch = input("Enter Student Branch: ")
        self.getColDet()
        self.getUnivDet()

    def disStudDet(self):
        self.dispUniDet()
        self.dispColDet()
        print("-"*50)
        print("\tStudent Roll No.: ",self.sno)
        print("\tStudent Name: ",self.sname)
        print("\tStudent Branch ",self.sbranch)

so = Student()
so.getStudDet()
so.disStudDet()