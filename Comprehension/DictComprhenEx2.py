# Write a python program which will accept list of +VE -VE numerical values and find squares of +VE numbers

print("-"*60)

sqlst = { int(val):int(val)**2 for val in input().split() if int(val) > 0 }
print("+VE number's Squares =",sqlst)
print("-"*60)