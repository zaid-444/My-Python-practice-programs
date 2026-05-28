# 3005. Count Elements With Maximum Frequency

def maxFrqcElem(nums):
    frqnc = []
    for num in nums:
        frqnc.append(nums.count(num))
    x = max(frqnc)
    s = 0
    for num in nums:
        if nums.count(num) == x:
            s += 1
    return s

nums = [ int(num) for num in input("Enter Numbers: ").split() ]
res = maxFrqcElem(nums)
print("~"*20)
print("Output:",res)
print("~"*20)