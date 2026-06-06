# 3131. Find the Integer Added to Array


def addedInteger(nums1,nums2):
    nums1.sort()
    nums2.sort()
    return nums2[0] - nums1[0]


nums1 = [ int(i) for i in input("Enter Nums1: ").split() ]
nums2 = [ int(i) for i in input("Enter Nums2: ").split() ]
print("~"*20)
print("Output:",addedInteger(nums1,nums2))
print("~"*20)