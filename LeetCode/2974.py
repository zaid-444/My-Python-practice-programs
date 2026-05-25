# 2974. Minimum Number Game

def numberGame(nums):
    nums.sort()
    arr = []
    while nums:
        arr.append(nums.pop(1))
        arr.append(nums.pop(0))
    return arr

nums = [ int(num) for num in input("Enter Numbers: ").split() ]

print("~"*40)
print("Before:",nums)
res = numberGame(nums)
print("After: ",res)
print("~"*40)