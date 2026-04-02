# Program for Demonstrating the need of Data Encapsulation--Data Member Level Through Instance Method

class Account:
    def getaccdata(self):
        self.__accno = 10
        self.cname = "Jacks"
        self.__bal = 80000.0
        self.__pin = 1234
        self.bname = "SBI"