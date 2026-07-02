# 121. Best Time to Buy and Sell Stock

# Brute
def maxProfit(prices):
    n = len(prices)
    mx_profit = 0
    for i in range(n):
        for j in range(i+1,n):
            if prices[i] < prices[j]:
                if prices[j]-prices[i] > mx_profit:
                    mx_profit = prices[j]-prices[i]
    return mx_profit



# Optimal
def maxProfit(prices):
    mx_profit = 0
    mn_price = float("inf")
    for n in prices:
        mn_price = min(mn_price,n)
        mx_profit = max(mx_profit,n-mn_price)
    return mx_profit



prices = [ int(i) for i in input("> ").split() ]

print("~"*20)
print(f"Output: {maxProfit(prices)}")
print("~"*20)