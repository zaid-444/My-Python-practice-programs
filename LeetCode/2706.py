# 2706. Buy Two Chocolates

def buyChoco(prices,money):
    prices.sort()
    if money >= (prices[0]+prices[1]):
        return money - (prices[0] + prices[1])
    else:
        return money
    
prices = [int(i) for i in input("Enter Prices of Chocolates: ").split()]
money = int(input('Enter Money: '))
res = buyChoco(prices,money)
print("~"*20)
print("Output:",res)
print("~"*20)