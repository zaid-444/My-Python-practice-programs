# 2696. Minimum String Length After Removing Substrings

def minLength(s):
    while "AB" in s or "CD" in s:
        s = s.replace("AB","")
        s = s.replace("CD","")
    return len(s)

s = input("> ")
res = minLength(s)
print("~"*20)
print("minLength:",res)
print("~"*20)