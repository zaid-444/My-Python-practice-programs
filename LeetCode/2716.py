# 2716. Minimize String Length

def minmzStrLen(s):
    res = ""
    for ch in s:
        if ch not in res:
            res += ch
    return len(res)

s = input("Enter a String: ")
res = minmzStrLen(s)
print("~"*30)
print("Output:",res)
print("~"*30)