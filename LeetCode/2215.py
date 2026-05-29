# 2215. Find the Difference of Two Arrays

def findDiff(nums1,nums2):
    lst = []
    l1 = []
    for n1 in nums1:            
        if n1 not in nums2 and n1 not in l1:
            l1.append(n1)

    l2 = []
    for n2 in nums2:            
        if n2 not in nums1 and n2 not in l2:
            l2.append(n2)
    lst.append(l1)
    lst.append(l2)
    return lst

nums1 = [ int(n) for n in input("Enter Value of Nums1: ").split() ]
nums2 = [ int(n) for n in input("Enter Value of Nums2: ").split() ]

res = findDiff(nums1,nums2)

print("~"*40)
print("Difference:",findDiff(nums1,nums2))
print("~"*40)