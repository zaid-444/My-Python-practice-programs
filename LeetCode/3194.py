# 3194. Minimum Average of Smallest and Largest Elements

def minimumAverage(nums):
    avg = []
    for i in range(len(nums)//2):
        mn = min(nums)
        mx = max(nums)
        nums.remove(mn)
        nums.remove(mx)
        avg.append((mn+mx)/2)
    return min(avg)

nums = [ int(n) for n in input("Enter Nums: ").split() ]

res = minimumAverage(nums)
print("~"*30)
print(f'Output: {res}')
print("~"*30)