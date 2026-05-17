# 1431. Kids With the Greatest Number of Candies

def kidsWithCandies(can,excan):
    mx = max(can)
    l = list()
    for i in can:
        if i + excan >= mx:
            l.append(True)
        else:
            l.append(False)
    return l

print("-"*50)
print("Enter List of Kids Candies")
can = [ int(i) for i in input().split() ]
excan = int(input("Enter Extra Candies: "))
print("-"*50)
res = kidsWithCandies(can,excan)
print("Output:",res)
print("-"*50)