# 1313. Decompress Run-Length Encoded 

def decompressRLElist(nums):
    lst = list()
    for i in range(0,len(nums),2):
        x = nums[i]
        for j in range(x):
            lst.append(nums[i+1])
    return lst

print("-"*50)
print("Enter list of Values")
nums = [ int(val) for val in input().split() ]
print("-"*50)
res = decompressRLElist(nums)
print("Output =",res)
print("-"*50)