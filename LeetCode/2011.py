# 2011. Final Value of Variable After Performing Operations

def finalVal(operations):
    res = 0
    for i in operations:
        if i == "++X" or i == "X++":
            res += 1
        else:
            res -= 1
    print("Final Result =",res)

print("-"*50)
print("Enter Your Operation's seprating with Space")
opr =  [ i for i in input().split() ]
print("-"*50)
finalVal(opr)
print("-"*50)