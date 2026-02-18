# Program for Demonstrating Decorators

def getval():
    return int(input("Enter number: "))

def square(zaid):
    def operation():
        n = zaid()
        return n,n**2
    return operation


op = square(getval)
n,sq = op()
print("Square of {} = {}".format(n,sq))