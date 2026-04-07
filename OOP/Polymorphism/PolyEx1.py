class Circle:
    def draw(self):
        print("Drawing Circle")
    

class Rect(Circle):
    def draw(self):
        print("Drawing Rect")
        super().draw()


class Square(Rect):
    def draw(self):
        print("Drawing Square")
        super().draw()


so = Square()
so.draw()