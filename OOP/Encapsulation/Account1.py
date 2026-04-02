# Program for Demonstrating the need of Data Encapsulation--Data Member Level Through Constructor

class Account:
    def __init__(self):
        self.__accno = 10
        self.cname = "Alex"
        self.__bal = 80000.0
        self.__pin = 1234
        self.bname = "SBI"