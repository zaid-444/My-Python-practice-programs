# Write a python Program which will accept any three numerical int values and find the biggest among them and check for equality by using simple if statemant

a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))
c = int(input("Enter Value of c: "))

if b == a == c:
    print("{}, {}, {} => All are Equal".format(a,b,c))

if b < a > c:
    print("{}, {}, {} => From this three value ({}) is biggest".format(a,b,c,a))

if a < b > c:
    print("{}, {}, {} => From this three value ({}) is biggest".format(a,b,c,b))

if a < c > b:
    print("{}, {}, {} => From this three value ({}) is biggest".format(a,b,c,c))