# 3162. Find the Number of Good Pairs 

def numberOfPairs(nums1,nums2,k):
    gpair = 0
    for n1 in nums1:
        for n2 in nums2:
            if n1 % (n2*k) == 0:
                gpair += 1
    print(f'Total Good Pairs =',gpair)

nums1 = [ int(n) for n in input("Enter Nums1: ").split() ]
nums2 = [ int(n) for n in input("Enter Nums2: ").split() ]
k = int(input("Enter Value of K: "))
print("~"*50)
numberOfPairs(nums1,nums2,k)
print("~"*50)