class Circle:
    def __init__(self,c):
        print("Drawing--",c)

class Square(Circle):
    def __init__(self,s):
        print("Drawing--",s)

class Rect(Square):
    def __init__(self, s=None):
        pass
    def area(self):
        print("Drawing--Rect")
        super().__init__("Square")
        Circle.__init__(self,"Circle")
        

ro = Rect()
ro.area() 