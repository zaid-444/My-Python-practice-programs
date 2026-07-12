# 1331. Rank Transform of an Array

def arrayRankTransform(arr):
    cp = arr.copy()
    cp.sort()
    d = {}
    rank = 1
    for val in cp:
        if val not in d:
            d[val] = rank
            rank += 1
    res = []
    for val in arr:
        res.append(d[val])
    return res


arr = [ int(i) for i in input("> ").split() ]
res = arrayRankTransform(arr)
print("~"*30)
print("Output:",res)
print("~"*30)