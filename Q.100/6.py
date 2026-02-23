# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# 	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# 	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

lst  = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(len(lst)):
    for j in range(len(lst)-1-i):
        if lst[j][-1] > lst[j+1][-1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]

print(lst)