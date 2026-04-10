class Circle:
    def __init__(self):
        print("Drawing Circle from Constructor")

class Rect(Circle):
    def __init__(self):
        print("Drawing Rect from Constructor")
        super().__init__()

class Square(Rect):
    def __init__(self):
        print("Drawing Square from Constructor")
        super().__init__()

so = Square()