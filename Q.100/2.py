# 2. Write a Python program to multiply all the items in a list.

lst = [2, 65, 8, 6, 5, 4, 1,]

mul = 1

for val in lst:
    mul = mul*val

print("-"*60)
print("List of Values  =",lst)
print("Multiply Values =",mul)
print("-"*60)