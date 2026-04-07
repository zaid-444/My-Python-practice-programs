class Circle:
    def drawcircle(self):
        print("Drawing Circle")
    
class Rect(Circle):
    def drawrect(self):
        print("Drawing Rectangle")

ro = Rect()
ro.drawcircle()
ro.drawrect()