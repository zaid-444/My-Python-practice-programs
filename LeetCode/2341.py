# 2341. Maximum Number of Pairs in Array

def numberOfPairs(nums):
    c = 0
    opr = 0
    s = set(nums)
    for num in s:
        cnt = nums.count(num)
        c += cnt%2
        opr += cnt//2
    return [opr,c]

nums = [ int(i) for i in input("Enter Numbers: ").split() ]
res = numberOfPairs(nums)
print("~"*30)
print("Output:",res)
print("~"*30)