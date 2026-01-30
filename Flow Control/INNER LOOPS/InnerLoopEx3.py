# for loop in while loop

i = 5

while i >= 1:
    print("Val of i-outer loop = {}".format(i))
    for j in range(3,0,-1):
        print("\tVal of j-inner loop = {}".format(j))
    else:
        print("\tOut of inner loop")
        i -= 1
else:
    print("\tOut of outer loop")