# Program for Generating Mul Table For a Given Number

class MulTable:
    def getval(self):
        while True:
            try:
                self.n = int(input("Enter any Number: "))
                if self.n > 0:
                    break
                else:
                    print("\tZero and -VE numbers Invalid")
            except ValueError:
                print("\tDon't Enter anything other than Number's")
    
    def gettable(self):
        self.getval()
        print("-"*20)
        print("Mul Table for",self.n)
        print("-"*20)
        for i in range(1,11):
            print("{} x {} = {}".format(self.n,i,self.n*i))
        print("-"*20)