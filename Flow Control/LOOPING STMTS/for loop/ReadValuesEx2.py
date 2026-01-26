# Write a python program which will read list of values from keyboard and display thos values

import sys

print("Enter Number of Values and Press @ to stop")

lst = []

while True:
    val = input("Enter value: ")
    if val == "@":
        print("Content of List =",lst)
        sys.exit()
    else:
        lst.append(float(val))