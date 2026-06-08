# 2367. Number of Arithmetic Triplets

def arithmeticTriplets(nums,diff):
    c = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                    c += 1
    return c

nums = [ int(i) for i in input("Enter numbers: ").split() ]
diff = int(input("Enter diff: "))
print("-"*30)
print("Output:",arithmeticTriplets(nums,diff))
print("-"*30)