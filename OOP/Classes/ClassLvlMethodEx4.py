class Employee:
    @classmethod
    def getcompdet(cls):
        cls.compname = "INFOSYS"
        cls.city = "PUNE"
    
    @classmethod
    def discompdet(cls):
        print("Comp Name: ",cls.compname)
        print("Comp City: ",Employee.city)

    def printcompdet(self):
        self.getcompdet()
        self.discompdet()


e1 = Employee()
e1.printcompdet()