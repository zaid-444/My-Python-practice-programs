# 1470. Shuffle the Array

def shuffle(nums,n):
    lst1 = nums[:len(nums)//2:]
    lst2 = nums[len(nums)//2::]
    lst = []
    for i in range(n):
        lst.append(lst1[i])
        lst.append(lst2[i])
    return lst

nums = [2,5,1,3,4,7]

res = shuffle(nums,3)
print("Input:",nums)
print("Output:",res)