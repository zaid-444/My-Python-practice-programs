# 2574. Left and Right Sum Differences

def lftRhtDiff(nums):
    lst = []
    for i in range(len(nums)):
        r_sum = sum(nums[i+1::])
        l_sum = sum(nums[:i:])
        if r_sum > l_sum:
            lst.append(r_sum-l_sum)
        else:
            lst.append(l_sum-r_sum)
    return lst


nums = [ int(num) for num in input("Enter Numbers: ").split() ]
res = lftRhtDiff(nums)
print("~"*30)
print("Output:",res)
print("~"*30)