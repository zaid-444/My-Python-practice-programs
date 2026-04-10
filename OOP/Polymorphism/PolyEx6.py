class Circle:
    def __init__(self):
        self.r = float(input("Enter Radius: "))
        self.ac = 3.14 * self.r ** 2
        print("Area of Circle:",self.ac)

class Square(Circle):
    def __init__(self):
        self.s = float(input("Enter Side: "))
        self.sa = self.s ** 2
        print("Area of Square:",self.sa)
        super().__init__()
        

class Rect(Square):
    def __init__(self):
        self.l = float(input("Enter Length: "))
        self.b = float(input("Enter Breadth: "))
        self.ra = self.l*self.b
        print("Area of RectAngle:",self.ra)
        super().__init__()

r = Rect()