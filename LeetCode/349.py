# 349. Intersection of Two Arrays

def intersection(nums1,nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    return list(nums1.intersection(nums2))


nums1 = [ int(i) for i in input("> ").split() ]
nums2 = [ int(i) for i in input("> ").split() ]
print("~"*20)
print("Output: {}".format(intersection(nums1,nums2)))
print("~"*20)