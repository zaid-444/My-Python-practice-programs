# Write a python program which will accept list of numerical values and obtain +VE even numbers

print("Enter list of Values separated by space")

lst = [ int(val) for val in input().split() ]

evenpos = list(filter(lambda num: num>2 and num%2==0,lst))
ngeven = list(filter(lambda num: num<0 and num%2==0,lst))

print("*"*50)
print("List of Values =",lst)
print("*"*50)
print("Even +VE numbers =",evenpos)
print("Even -VE numbers =",ngeven)
print("*"*50)