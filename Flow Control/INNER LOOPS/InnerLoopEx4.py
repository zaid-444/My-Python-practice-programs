# while loop in for loop

for i in range(5,0,-1):
    print("Value of i-outer loop = {}".format(i))
    j = 1
    while j <= 3:
        print("\tVal of j-inner loop = {}".format(j))
        j += 1