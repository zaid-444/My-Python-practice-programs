# 1051. Height Checker

def heightChecker(heights):
    lst = heights.copy()
    lst.sort()
    c = 0
    for i in range(len(heights)):
        if heights[i] != lst[i]:
            c += 1
    return c

heights = [ int(ht) for ht in input("Enter Heights: ").split() ]
res = heightChecker(heights)
print("Output:",res)