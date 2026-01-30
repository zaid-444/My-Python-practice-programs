# Write a python program which will display one to n multiplication tables

n = int(input("How Many Mul tables u want: "))

if n <= 0:
    print("{} is Invalid input".format(n))
else:
    for i in range(1,n+1):
        print("-"*20)
        print("Mul Table for {}".format(i))
        print("-"*20)
        for j in range(1,11):
            print("{} x {} = {}".format(i,j,i*j))