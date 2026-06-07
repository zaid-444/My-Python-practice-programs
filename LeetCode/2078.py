# 2078. Two Furthest Houses With Different Colors

def maxDistance(colors):
    mxdiff = 0
    for i in range(len(colors)):
        for j in range(i+1,len(colors)):
            if colors[i] != colors[j]:
                diff = j - i
                if mxdiff < diff:
                    mxdiff = diff
    return mxdiff

prices = [ int(i) for i in input("Enter Colors of House: ").split() ]
print("~"*20)
print("Output:",maxDistance(prices))
print("~"*20)