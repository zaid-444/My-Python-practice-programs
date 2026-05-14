# 1512. Numbers of Good Pairs

def numIdenticalPairs(nums):
    c = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                c += 1
    return c

print("-"*50)
print("Enter List Values Separated by Space")
nums = [ int(i) for i in input().split() ]
print("-"*50)
res = numIdenticalPairs(nums)
print("Your List =",nums)
print("Good Pairs =",res)
print("-"*50)