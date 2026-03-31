# Program for Demonstrating Parameterized Constructor

class Test:
    def __init__(self,a,b):
        print("I am from Parameterized Constructor")
        self.a = a
        self.b = b
        print("Value of A =",self.a)
        print("Value of B =",self.b)
        print("-----------------------------------")

t1 = Test(10,20)
t2 = Test("Zaid","Jaahil")
t3 = Test(1000,"Rohit")