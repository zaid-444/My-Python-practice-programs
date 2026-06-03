# 3079. Find the Sum of Encrypted Integers

def sumOfEncryptedInt(nums):
    s = 0
    for num in nums:
        str_num = str(num)
        mx = max(str_num)
        x = int(mx*len(str_num))
        s += x
    return s

nums = [ int(i) for i in input("Enter Nums: ").split() ]
print("~"*20)
res = sumOfEncryptedInt(nums)
print("Output:",res)
print("~"*20)