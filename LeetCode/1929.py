# 1929. Concatenation of Array

def getConcatenation(nums):
    return nums + nums

print("-"*50)
print("Enter List nums Separated by space...")
lst = [ int(val) for val in input().split() ]
print("-"*50)
print("List =",lst)
print("Final Result =",getConcatenation(lst))
print("-"*50)