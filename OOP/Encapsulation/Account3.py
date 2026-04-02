# Program for Demonstrating the need of Data Encapsulation--Data Member Level Through Instance Method

class Account:
    def __getaccdata(self): # Instance Method - encapsulation
        self.accno = 10
        self.cname = "Jacks"
        self.bal = 80000.0
        self.pin = 1234
        self.bname = "SBI"