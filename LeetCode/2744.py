# 2744. Find Maximum Number of String Pairs

def maxNumofStr(words):
    c = 0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i] == words[j][::-1]:
                c += 1
    return c

words = [ w for w in input("Enter Words: ").split() ]

res = maxNumofStr(words)
print("~"*30)
print("Number of String Pairs: ",res)
print("~"*30)