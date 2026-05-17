# 2824. Count Pairs Whose Sum is Less than Target

def countPairs(nums,target):
    Sum = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] < target:
                Sum += 1
    print("Pairs =",Sum)

print("-"*50)
print("Enter List Values Separated by Space")
nums = [ int(i) for i in input().split() ]
target = int(input("Enter Target Value: "))
print("-"*50)
countPairs(nums,target)
print("-"*50)