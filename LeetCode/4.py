# 4. Median of Two Sorted Arrays

def findMedSortedArr(nums1,nums2):
    lst = []
    l_index = 0
    r_index = 0
    l_len = len(nums1)
    r_len = len(nums2)
    while r_len > r_index and l_len > l_index:
        if nums1[l_index] <= nums2[r_index]:
            lst.append(nums1[l_index])
            l_index += 1
        else:
            lst.append(nums2[r_index])
            r_index += 1
    if l_len > l_index:
        while l_index < l_len:
            lst.append(nums1[l_index])
            l_index += 1
    if r_len > r_index:
        while r_index < r_len:
            lst.append(nums2[r_index])
            r_index += 1

    n = len(lst)
    mid = n//2
    if n%2 == 1:
        return lst[mid]
    else:
        return (lst[mid-1]+lst[mid])/2
    

nums1 = [ int(i) for i in input("> ").split() ]
nums2 = [ int(i) for i in input("> ").split() ]
print("~"*20)
print(f"Output: {findMedSortedArr(nums1,nums2)}")
print("~"*20)