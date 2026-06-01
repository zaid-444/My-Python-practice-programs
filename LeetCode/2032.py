# 2032. Two Out of Three

def twoOutOfThree(nums1,nums2,nums3):
    s1 = set(nums1)
    s2 = set(nums2)
    s3 = set(nums3)
    lst = []
    for num in s1:
        if num in s2 or num in s3:
            lst.append(num)
    for num in s2:
        if num in s3 and num not in lst:
            lst.append(num)
    return lst

nums1 = [ int(num) for num in input("Enter nums1: ").split() ]
nums2 = [ int(num) for num in input("Enter nums2: ").split() ]
nums3 = [ int(num) for num in input("Enter nums3: ").split() ]
print("~"*30)
print("Output:",twoOutOfThree(nums1,nums2,nums3))
print("~"*30)