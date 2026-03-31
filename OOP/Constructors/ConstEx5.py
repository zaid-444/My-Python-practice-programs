# Program for Demonstrating Both Default and Parameterized Constructor

class Test:
    def __init__(self,a=1,b=2):
        print("I am from Default / Parameterized Constructor")
        self.a = a
        self.b = b
        print("Value of A =",self.a)
        print("Value of B =",self.b)
        print("---------------------------------------------")

t1 = Test() # Default Constructor
t2 = Test(199,299)
t3 = Test(b="Zaid")