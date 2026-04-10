class Circle:
    def __init__(self,r):
        self.ac = 3.14 * r ** 2
        print("Area of Circle:",self.ac)

class Square:
    def __init__(self,s):
        self.sa = s ** 2
        print("Area of Square:",self.sa)
        

class Rect(Square,Circle):
    def __init__(self,l,b):
        self.ra = l*b
        print("Area of RectAngle:",self.ra)
        print("-------------------------------------")
        super().__init__(float(input("Enter Side: ")))
        print("-------------------------------------")
        Circle.__init__(self,float(input("Enter Radius: ")))


l = float(input("Enter Length: "))
b = float(input("Enter Breadth: "))

ro = Rect(l,b)