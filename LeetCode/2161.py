# 2161. Partition Array According to Given Pivot

def pivotArray(nums,pivot):
    left = []
    middle = []
    right = []
    for num in nums:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            middle.append(num)
    return left + middle + right

nums = [ int(i) for i in input("Enter nums: ").split() ]
pivot = int(input("Enter value of Pivot: "))

res = pivotArray(nums,pivot)

print("-"*50)
print(f"pivotArray: {res}")
print("-"*50)