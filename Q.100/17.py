# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

lst = [ num ** 2 for num in range(1,31) ]

lst = lst[5:]
# print(lst)

print("-"*100)
for i in lst:
    print(i,end=" ")
print()
print("-"*100)