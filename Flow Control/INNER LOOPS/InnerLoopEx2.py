# while loop in while loop

i = 1

while i<6:
    print("Value of i-outer loop = {}".format(i))
    j = 1
    while j < 4:
        print("\tValue of j-inner loop = {}".format(j))
        j += 1
    else:
        print("\tOut-off inner loop")
        i += 1
else:
    print("Out-off outer loop")