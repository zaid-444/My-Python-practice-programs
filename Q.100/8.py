# 8. Write a Python program to check a list is empty or not.

print("Enter a list of values separated by space")

lst = [ i for i in input().split() ]

print("-"*50)
if lst:
    print("List is Not Empty")
    print("Element of list =",lst)
else:
    print("List is Empty")
print("-"*50)