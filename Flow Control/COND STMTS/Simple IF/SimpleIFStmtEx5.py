# Write a python Program which will accept any three numerical int values and find the Smallest among them and check for equality by using simple if statemant

a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))
c = int(input("Enter Value of c: "))

if a == b and b == c:
    print("All are Equal Numbers")

if a < b and a < c:
    print("{}, {}, {} => From this three Numbers ({}) is Smallest".format(a,b,c,a))

if b < c and b < a:
    print("{}, {}, {} => From this three Numbers ({}) is Smallest".format(a,b,c,b))

if c < a and c < b:
    print("{}, {}, {} => From this three Numbers ({}) is Smallest".format(a,b,c,c))