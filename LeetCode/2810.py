# 2810. Faulty Keyboard

def finalStr(s):
    res = ""
    for ch in s:
        if ch == "i":
            res = res[::-1]
        else:
            res += ch
    return res

s = input("Enter Anything: ")
print("~"*30)
res = finalStr(s)
print("Output:",res)
print("~"*30)