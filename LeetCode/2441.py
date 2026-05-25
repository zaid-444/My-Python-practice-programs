# 2441. Largest Positive Integer That Exists With Its Negative

def findMaxK(nums):
    ans = -1
    for num in nums:
        if -num in nums:
            ans = max(ans,abs(num))
    return ans

nums = [ int(num) for num in input("Enter Numbers: ").split() ]
res = findMaxK(nums)
print("Output:",res)