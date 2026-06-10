# 2085. Count Common Words With One Occurrence


def countWords(words1,words2):
    d1 = {}
    d2 = {}
    for w in words1:
        if w in d1:
            d1[w] += 1
        else:
            d1[w] = 1
    for w in words2:
        if w in d2:
            d2[w] += 1
        else:
            d2[w] = 1
    c = 0
    for w in d1:
        if d1[w] == 1 and d2.get(w,0) == 1:
            c += 1
    return c

words1 = [ i for i in input("Enter Words1: ").split() ]
words2 = [ i for i in input("Enter Words2: ").split() ]
res = countWords(words1,words2)

print("~"*15)
print("Output:",res)
print("~"*15)