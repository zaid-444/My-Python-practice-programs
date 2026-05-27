# 3028. Ant on the Boundary

def returnToBoundaryCount(nums):
    curr_ant = 0
    c = 0
    for num in nums:
        curr_ant += num
        if curr_ant == 0:
            c += 1
    print("Ant on the Boudary {} time".format(c))

nums = [ int(n) for n in input("Enter Nums: ").split() ]
returnToBoundaryCount(nums)