class Account:
    def __init__(self): # Instance Method - encapsulation
        self.__accno = 10
        self.cname = "Jacks"
        self.__bal = 80000.0
        self.__pin = 1234
        self.bname = "SBI"
    def showdetails(self):
        print("-"*30)
        print("Account Number =",self.__accno)
        print("Account Name   =",self.cname)
        print("Account Bal    =",self.__bal)
        print("Account Pin    =",self.__pin)
        print("Account Branch =",self.bname)
        print("-"*30)

ac = Account()
ac.showdetails()