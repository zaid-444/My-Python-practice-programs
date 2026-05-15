# 1920. Build Array from Permutation

def buildList(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans


print("-"*50)
print("Enter List Values Separated by Space")
nums = [ int(i) for i in input().split() ]
print("-"*50)

res = buildList(nums)
print("Befor List Permutation =",nums)
print("List Permutation =",res)
print("-"*50)