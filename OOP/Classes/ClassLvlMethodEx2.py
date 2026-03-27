class Employee:
    @classmethod
    def getcompdet(cls):
        cls.compname = "INFOSYS"
        cls.city = "PUNE"
    
    @classmethod
    def discompdet(cls):
        cls.getcompdet()
        print("Comp Name: ",cls.compname)
        print("Comp City: ",Employee.city)


Employee.discompdet()