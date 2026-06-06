# 2455. Average Value of Even Numbers That Are Divisible by Three

def averageValue(nums):
    lst = []
    for num in nums:
        if num%2 == 0 and num%3 == 0:
            lst.append(num)
    if lst:
        return sum(lst)//len(lst)
    else:
        return 0
    

nums = [ int(i) for i in input("Enter Nums: ").split() ]
print("~"*20)
print("Output:",averageValue(nums))
print("~"*20)