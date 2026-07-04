# 48. Rotate Image

# TC--> O(nx2) SC--> O(1)
def rotate(matrix):
    n = len(matrix)
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for row in matrix:
        row.reverse()
    
    # Only for testing purpose
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            print(matrix[i][j],end="  ")
        print()

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print("~"*20)
rotate(matrix)
print("~"*20)