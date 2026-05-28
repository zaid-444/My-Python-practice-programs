# 2465. Number of Distinct Averages

def distinctAvg(nums):
    i = 0
    s = set()
    while i < len(nums)//2:
        mn = nums[i]
        mx = nums[len(nums)-1-i]
        s.add((mn+mx)/2)
        i += 1
    return len(s)


nums = [ int(num) for num in input("Enter Numbers: ").split() ]
res = distinctAvg(nums)

print("~"*20)
print("Output:",res)
print("~"*20)