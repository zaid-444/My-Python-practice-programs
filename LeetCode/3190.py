# 3190. Find Minimum Operations to Make All Elements Divisible by Three

def minimumOpr(nums):
    opr = 0
    for num in nums:
        if num%3 == 0:
            continue
        else:
            opr += 1
    print("Minimum Operations =",opr)

print("-"*50)
nums = [ int(i) for i in input("Enter Nums: ").split() ]
print("-"*50)
minimumOpr(nums)
print("-"*50)