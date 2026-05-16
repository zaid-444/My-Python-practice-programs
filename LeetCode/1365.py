# 1365. How Many Numbers Are Smaller Than the Current Number

def smallerNumThnCurr(nums):
    l = []
    for i in range(len(nums)):
        c = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                c += 1
        l.append(c)

    # for i in nums:
    #     c = 0
    #     for j in nums:
    #         if i > j:     # Second Method
    #             c += 1
    #     l.append(c)

    return l

print("-"*50)
print("Enter List Values Separated by Space")
nums = [ int(i) for i in input().split() ]
print("-"*50)

res = smallerNumThnCurr(nums)
print("List Values =",nums)
print("Smaller Numbers =",res)
print("-"*50)