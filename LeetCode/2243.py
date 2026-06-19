# 2243. Calculate Digit Sum of a String

def digitSum(s,k):
    while len(s) > k:
        n = ""
        for i in range(0,len(s),k):
            a = s[i:i+k]
            sm = 0
            for d in a:
                sm += int(d)
            n += str(sm)
        s = n
    return s

s = "11111222223"
k = 3

print("~"*30)
print("Output:",digitSum(s,k))
print("~"*30)