# Write a python program which will accept any numerical value and decide whether it is positive or nigative or zero

n = int(input("Enter Any Number: "))

if n>0:
    print("{} is +VE number".format(n))

if n<0:
    print("{} is -VE number".format(n))

if n==0:
    print("{} is Zero".format(n))

print("Program Completed")