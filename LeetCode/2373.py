# 2373. Largest Local Value in a Matrix

def largestLocal(grid):
    lst = []
    for i in range(len(grid)-2):
        temp = []
        for j in range(len(grid)-2):
            temp.append(max(grid[i][j],grid[i][j+1],grid[i][j+2],
                            grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                            grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]))
        lst.append(temp)
    return lst

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
res = largestLocal(grid)
print("~"*30)
print("Output:",res)
print("~"*30)