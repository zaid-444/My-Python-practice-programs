# 2643. Row With Maximum Ones

def rowAndMaxOnes(mat):
    lst = []
    indx = 0
    no1 = 0
    for i,v in enumerate(mat):
        ones = v.count(1)
        if ones > no1:
            no1 = ones
            indx = i
    lst.append(indx)
    lst.append(no1)
    return lst

mat = [[0,0],[1,1],[0,0]]
print("-"*30)
print("Output:",rowAndMaxOnes(mat))
print("-"*30)