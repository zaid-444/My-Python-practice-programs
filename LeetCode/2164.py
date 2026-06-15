# 2164. Sort Even and Odd Indices Independently

def sortEvenOdd(nums):
    odd = []
    even = []
    for i in range(len(nums)):
        if i%2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    odd.sort(reverse=True)
    even.sort()
    lst = []
    e = 0
    o = 0
    for i in range(len(nums)):
        if i%2 == 0:
            lst.append(even[e])
            e += 1
        else:
            lst.append(odd[o])
            o += 1
    return lst


nums = [ int(i) for i in input("Enter nums: ").split() ]

print("~"*50)
print(f"Output: {sortEvenOdd(nums)}")
print("~"*50)