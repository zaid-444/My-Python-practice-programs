# 73. Set Matrix Zeroes


# Brute     TC--> O(Mxn)x(M+N)  SC--> O(1)
def markInfinity(matrix,row,col):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        if matrix[i][col] != 0:
            matrix[i][col] = float("inf")
    for i in range(c):
        if matrix[row][i] != 0:
            matrix[row][i] = float("inf")


def setZeros(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):          # O(N x M)
        for j in range(c):
            if matrix[i][j] == 0:       # O(N + M)
                markInfinity(matrix,i,j)
    for i in range(r):        #O(N x M)      
        for j in range(c): 
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0

    # Only for testing purpose
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end="  ")
        print()


# Optimal       TC--> O(2(MxN)) = O(MxN)        SC--> O(M + N)
def setZeros(matrix):
    row = len(matrix)
    col = len(matrix[0])
    rowTrack = [ 0 for _ in range(row) ]
    colTrack = [ 0 for _ in range(col) ]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                rowTrack[i] = -1
                colTrack[j] = -1
    for i in range(row):
        for j in range(col):
            if rowTrack[i] == -1 or colTrack[j] == -1:
                matrix[i][j] = 0
    
    # Only for testing purpose
    for i in range(row):
        for j in range(col):
            print(matrix[i][j],end="  ")
        print()





matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print("~"*20)
setZeros(matrix)
print("~"*20)