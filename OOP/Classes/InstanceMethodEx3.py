# Program for adding two numbers

class Addop:
    def getvalues(self):
        self.a = int(input("Enter value of a: "))
        self.b = int(input("Enter Value of b: "))
    def addvalues(self):
        self.c = self.a + self.b
    def disvalues(self):
        print(self.a)
        print(self.b)
        print(self.c)

a1 = Addop()
a1.getvalues()
a1.addvalues()
a1.disvalues()