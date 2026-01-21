# Write a python Program which will decide even or odd for positive numbers only but not for negative numbers

n = int(input("Enter any Number: "))

if n<0:
    print("{} is invalide number".format(n))

if n%2==0 and n>0:
    print("{} is Even number".format(n))

if n%2!=0 and n>0:
    print("{} is Odd number".format(n))




