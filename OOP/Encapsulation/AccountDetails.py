class Account:
    def __getaccdata(self): # Instance Method - encapsulation
        self.accno = 10
        self.cname = "Jacks"
        self.bal = 80000.0
        self.pin = 1234
        self.bname = "SBI"
    def showdetails(self):
        self.__getaccdata()
        print(self.__dict__)

ac = Account()
ac.showdetails()