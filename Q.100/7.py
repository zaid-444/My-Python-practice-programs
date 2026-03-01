# 7. Write a Python program to remove duplicates from a list.

print("Enter a list of values separated by space")

lst = [ int(i) for i in input().split() ]

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print("-"*50)
print("Before removing duplicates")
print(lst)
print("-"*50)
print("After removing duplicates")
print(unique)
print("-"*50)