# Program for Calculating Factorial of a Number by using Classes and Object with Constructor

class Factorial:
    def __init__(self,n):
        self.n = n
    
    def fact(self):
        fa = 1
        if self.n < 0:
            print("-"*40)
            print("For -VE Number Factorial Does not Exist")
        else:
            for i in range(1,self.n+1):
                fa = fa * i
            print("-"*40)
            print("Factorial of {} = {}".format(self.n,fa))
            print("-"*40)


print("-"*40)
try:
    f = Factorial(int(input("Enter a number for Calculating Factorial: ")))
    f.fact()
except ValueError:
    print("Don't Enter other than Numbers")