# 3289. The Two Sneaky Numbers of Digitville

def getSneakyNumbers(nums):
    lst = []
    for n in nums:
        c = nums.count(n)
        if c > 1:
            if n not in lst:
                lst.append(n)
    return lst

nums = [ int(n) for n in input("Enter Nums: ").split() ]
print("~"*50)
print("Output:",getSneakyNumbers(nums))
print("~"*50)