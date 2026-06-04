# 3174. Clear Digits

def clearDigits(s):
    lst = []
    for v in s:
        if v.isdigit():
            lst.pop()
        else:
            lst.append(v)
    return "".join(lst)


s = input("Enter any String: ")
res = clearDigits(s)
print("~"*30)
print("Result:",res)
print("~"*30)