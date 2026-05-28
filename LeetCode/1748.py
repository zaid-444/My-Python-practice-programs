# 1748. Sum of unique Elements

def sumOfUnique(nums):
    s = 0
    for num in nums:
        if num in nums and nums.count(num) == 1:
            s += num
    print("Sum of Unique Elements:",s)

nums = [ int(num) for num in input("Enter Numbers: ").split() ]
print("~"*30)
sumOfUnique(nums)
print("~"*30)