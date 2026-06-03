# 2965. Find Missing and Repeated Values

def fun(grid):
    lst = list()
    for row in grid:
        lst.extend(row)
    
    repeat = 0
    missing = 0
    for i in range(1,len(lst)+1):
        if lst.count(i) == 2:
            repeat = i
        elif i not in lst:
            missing = i
    return [repeat,missing]



print("~"*20)
print("Output:",fun([[9,1,7],[8,9,2],[3,4,6]]))
print("~"*20)