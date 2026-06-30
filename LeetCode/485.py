# 485. Max Consecutive Ones

def func(nums):
    count = 0
    mx = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            mx = max(count,mx)
            count = 0
    return max(count,mx)

nums = [ int(i) for i in input("> ").split() ]
print("~"*20)
print(f"Output: {func(nums)}")
print("~"*20)