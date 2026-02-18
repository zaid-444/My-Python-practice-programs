def cube(sq):
    def cal():
        n,m = sq()
        res = n**3
        return n,m,res
    return cal


def square(pv):
    def cal():
        n = pv()
        res = n**2
        return n,res
    return cal

@cube
@square
def getval():
    return int(input("Enter a number: "))

n,sq,cub = getval()
print("Square of {} = {}".format(n,sq))
print("Cube of {} = {}".format(n,cub))