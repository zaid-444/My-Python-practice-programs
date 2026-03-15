# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

print("Enter The numbers")

lst = [ n for n in input().split() if int(n)%2 != 0]

print()

for num in lst:
    print(num)