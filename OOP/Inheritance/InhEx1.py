class C1:
    def disp1(self):
        print("C1--disp1()--Instance Method")

class C2(C1):
    def disp2(self):
        print("C2--disp2()--Instance Method")

o2 = C2()
o2.disp2()
o2.disp1()