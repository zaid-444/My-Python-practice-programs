# 3432. Count Partitions with Even Sum Difference

def countPartitions(nums):
    c = 0
    for i in range(len(nums)-1):
        if (sum(nums[0:i+1]) - sum(nums[i+1:]))%2 == 0:
            c += 1
    return c

nums = [ int(num) for num in input("Enter Numbers: ").split() ]
print("Total Partitions:",countPartitions(nums))