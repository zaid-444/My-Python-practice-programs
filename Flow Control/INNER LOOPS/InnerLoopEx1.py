# for loop in for loop

for i in range(1,6):
    print("Value of i-outer loop = {}".format(i))
    for j in range(1,4):
        print("\tValue of j-inner loop = {}".format(j))
    else:
        print("\tOut-off inner loop")
else:
    print("Out-off outer loop")