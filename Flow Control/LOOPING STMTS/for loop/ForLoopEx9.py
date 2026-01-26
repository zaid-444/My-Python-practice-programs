# write a python program which will print multiplys of three within the given range

n = int(input("Enter any number: "))

if n <=0:
    print("{} is invalid input".format(n))
else:
    for i in range(1,n+1):
        if i%3 == 0:
            print(i)