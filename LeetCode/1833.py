# 1833. Maximum Ice Cream Bars

def maxIceCream(costs,coins):
    c = 0
    costs.sort()
    for i in costs:
        if i > coins:
            break
        else:
            c += 1
            coins -= i
    return c


costs = [ int(i) for i in input("> ").split() ]
coins = int(input("Enter coins: "))

print("~"*15)
print("Total:",maxIceCream(costs,coins))
print("~"*15)