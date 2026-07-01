# 2138. Divide a String Into Group of Size k

def divideString(s,k,fill):
    # lst = [ s[i:i+k] for i in range(0,len(s),k) ]
    lst = []
    for i in range(0,len(s),k):
        lst.append(s[i:i+k])
    n = len(lst[-1])
    if n != k:
        lst[-1] = lst[-1] + fill*(k-n)
    return lst


s = "abcdefghij"
k = 3
fill = "x"
print("~"*40)
print(f"Output: {divideString(s,k,fill)}")
print("~"*40)