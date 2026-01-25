# Write a python Program which will generate n to 1 where n is +VE int value

n = int(input("Enter any number: "))

if n <= 0:
    print("{} Invalid input".format(n))
else:
    while n >= 1:
        print("\t",n)
        n -= 1