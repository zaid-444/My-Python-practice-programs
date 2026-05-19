# 1572. Matrix Diagonal Sum

def diagonalSum(mat):
    s = 0
    n = len(mat)
    for i in range(n):
        s += mat[i][i]
        if i != n-i-1:
            s += mat[i][n-i-1]
    return s


mat = [[1,2,3],[4,5,6],[7,8,9]]
res = diagonalSum(mat)
print("-"*30)
print("Output:",res)
print("-"*30)