# Program for Demonstrating Default Constructor

class Test:
    def __init__(self):
        self.a = "abc"
        self.b = "xyz"
        print("I am From Default Constructor")
        print("Val of A =",self.a)
        print("Val of B =",self.b)
        print("-----------------------------")

t1 = Test()
t2 = Test()