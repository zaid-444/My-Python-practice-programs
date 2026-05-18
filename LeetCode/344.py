# 344. Reverse String

def reverseString(s):
    f = 0
    l = len(s) - 1
    while f < l:
        s[f],s[l] = s[l],s[f]
        f += 1
        l -= 1
    return s

res = reverseString(['h','e','l','l','o'])
print(res)