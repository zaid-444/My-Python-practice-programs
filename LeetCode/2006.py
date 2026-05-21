# 2006. Count Number of Pairs With Absolute Difference K

def countKDifference(nums,k):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                if nums[i] - nums[j] == k:
                    count += 1
            else:
                if nums[j] - nums[i] == k:
                    count += 1
    print("Count of Pairs With Difference K =",count)

nums = [ int(i) for i in input("Enter Nums: ").split() ]
k = int(input("Enter Value of K: "))

print("-"*50)
countKDifference(nums,k)
print("-"*50)