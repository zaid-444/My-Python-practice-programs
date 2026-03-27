# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

lst = [ num**2 for num in range(1,31) ]
# f = list()
# l = list()
# f.extend(lst[0:5])
# l.extend(lst[-5:])
# fl = f+l
# print(fl)

firstlast = []

for i in range(len(lst)):
    if i in(0,1,2,3,4,25,26,27,28,29):
        firstlast.append(lst[i])

print(firstlast)