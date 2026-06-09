# 2206. Divide Array Into Equal Pairs

def divideArray(nums):
    s = set(nums)
    for val in s:
        if nums.count(val)%2 != 0:
            return False
    return True

nums = [ int(i) for i in input("Enter nums: ").split() ]

res = divideArray(nums)

print("~"*20)
print(f"Output: {res}")
print("~"*20)