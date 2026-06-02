# 2053. Kth Distinct String in an Array

def kthDistinct(arr,k):
    lst = []
    for v in arr:
        if arr.count(v) == 1:
            lst.append(v)
    if len(lst) >= k:
        return lst[k-1]
    else:
        return ""
    
arr = [ val for val in input("Enter Arr: ").split() ]
k = int(input("Enter Value of k: "))
res = kthDistinct(arr,k)
print("~"*20)
print("Result:",res)
print("~"*20)