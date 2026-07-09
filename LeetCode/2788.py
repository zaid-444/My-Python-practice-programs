# 2788. Split String by Separator

def splitWords(words,separator):
    lst = []
    ans = []
    for i in words:
        l = i.split(separator)
        if len(l) > 0:
            lst.extend(l)
    for i in lst:
        if i:
            ans.append(i)
    print(ans)


words = ["$easy$","$problem$"]
separator = "$"

splitWords(words,separator)