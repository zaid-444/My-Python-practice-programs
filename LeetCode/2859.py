# 2859. Sum of Values at Indices With K set bits

def sumIndices(nums,k):
    s = 0
    for i in range(len(nums)):
        if bin(i).count("1") == k:
            s += nums[i]
    return s



nums = [ int(num) for num in input("Enter Numbers: ").split() ]
k = int(input("Enter Value of K: "))

print("~"*20)
print("Output:",sumIndices(nums,k))
print("~"*20)