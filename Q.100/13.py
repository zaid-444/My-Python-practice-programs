# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

for i in range(3):
    print("Layer {}".format(i+1))
    for j in range(4):
        for k in range(6):
            print("*",end=" ")
        print()
    print()