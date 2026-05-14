# 1672. Richest Customer Wealth

def maximumWealth(accns):
    mx = 0
    for i in accns:
        s = 0
        for j in i:
            s += j
        if mx <= s:
            mx = s
    print("The richest customer wealth is =",mx)

print("-"*50)
accns = [[1,2,3],[3,2,1]]
maximumWealth(accns)
print("-"*50)
