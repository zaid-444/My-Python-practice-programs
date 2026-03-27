# Program for Demonstrating Class Level Method


class Employee:
    @classmethod
    def getcompdet(cls): # Class Level Method
        cls.compname = "WIPRO"
        cls.city = "PUNE"
    
    @classmethod
    def discompdet(cls):
        print("Comp Name: ",cls.compname)
        print("Comp City: ",Employee.city)

Employee.getcompdet()
Employee.discompdet()