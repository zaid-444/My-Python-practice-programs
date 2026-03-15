# 15. Write a Python program to shuffle and print a specified list.

lst = [1,2,3,4,5]
print(lst)

lst[0],lst[3] = lst[3],lst[0]
lst[4],lst[2] = lst[2],lst[4]

print(lst)