# Write a python program which will accept a number and calculate its factorial by using anonymous function

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact

print("-"*50)
num = int(input("Enter a number to check factorial: "))
fact = lambda num: factorial(num)
print("-"*50)
factnum = fact(num)
print("Factorial of => {} = {}".format(num,factnum))
print("-"*50)
