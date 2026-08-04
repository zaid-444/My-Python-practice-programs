# 378. Kth Smallest Element in a Sorted Matrix

def kthSmallest(matrix,k):
    lst = []
    for row in matrix:
        lst.extend(row)
    lst.sort()
    return lst[k-1]