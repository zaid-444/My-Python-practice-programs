# 9. Write a Python program to clone or copy a list.

print("Enter a list of values separated by space")

lst = [ val for val in input().split() ]

print("-"*50)
print("Original List =",lst)
print("-"*50)

clone = lst.copy()

print("Copied List =",clone)
print("-"*50)