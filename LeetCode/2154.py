# 2145. Keep Multiplying Found Values by Two

def findFinalValue(nums,original):
    while original in nums:
        original = original * 2
    return original



nums = [ int(i) for i in input("Enter Numbers: ").split() ]
original = int(input("Enter a original: "))
res = findFinalValue(nums,original)
print("~"*30)
print("Original:",res)
print("~"*30)