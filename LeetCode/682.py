# 682. Baseball Game

def calPoints(operations):
    lst = []
    for ops in operations:
        if ops == "C":
            lst.pop()
        elif ops == "D":
            lst.append(lst[-1]*2)
        elif ops == "+":
            lst.append(lst[-1]+lst[-2])
        else:
            lst.append(int(ops))
    return sum(lst)


ops = ["5","-2","4","C","D","9","+","+"]
res = calPoints(ops)
print("~"*20)
print("Output:",res)
print("~"*20)