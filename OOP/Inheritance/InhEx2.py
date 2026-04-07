class C1:
    def getA(self):
        self.a = int(input("Enter the value of a: "))

class C2:
    def getB(self):
        self.b = int(input("Enter the value of b: "))

class C3(C1,C2):
    def operation(self):
        self.c = self.a + self.b
    def disresult(self):
        print(f'{self.a} + {self.b} = {self.c}')

o3 = C3()
o3.getA()
o3.getB()
o3.operation()
print("------------------")
o3.disresult()