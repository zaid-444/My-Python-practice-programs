# 1460. Make Two Arrays Equal by Reversing Subaarays

def canBeEqual(target,arr):
    target.sort()
    arr.sort()
    return target == arr

target = [ int(n) for n in input("Enter target List Elements: ").split() ]
arr = [ int(n) for n in input("Enter arr List Elements: ").split() ]
res = canBeEqual(target,arr)
print("~"*30)
print("Output:",res)
print("~"*30)