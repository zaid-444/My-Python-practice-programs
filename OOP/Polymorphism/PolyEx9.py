class Circle:
    def __init__(self):
        print("Drawing--Circle")

class Square(Circle):
    def __init__(self):
        print("Drawing--Square")

class Rect(Square):
    def area(self):
        print("Drawing--Rect")
        

ro = Rect()
ro.area()