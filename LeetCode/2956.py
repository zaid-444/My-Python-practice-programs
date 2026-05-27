# 2956. Find Common Elements Between Two Arrays

def xyz(nums1,nums2):
    c1 = 0
    c2 = 0
    lst = []
    for num in nums1:
        if num in nums2:
            c1 += 1
    for num in nums2:
        if num in nums1:
            c2 += 1
    lst.append(c1)
    lst.append(c2)
    return lst

nums1 = [ int(n) for n in input("Enter Nums1: ").split() ]
nums2 = [ int(n) for n in input("Enter Nums2: ").split() ]
print("Common Elements:",xyz(nums1,nums2))