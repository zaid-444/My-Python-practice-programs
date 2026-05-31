# 3300. Minimum Element After Replacement With Digit Sum

def minElement(nums):
    a = max(nums)
    for num in nums:
        k = 0
        for n in str(num):
            k += int(n)
        if k < a:
            a = k
    return a


nums = [ int(n) for n in input("Enter Nums: ").split() ]
print("~"*50)
print("Output:",minElement(nums))
print("~"*50)