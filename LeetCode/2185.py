# 2185. Counting Words With a Given Prefix

def prefixCount(words,pref):
    count = 0
    for word in words:
        if word.startswith(pref):
            count += 1
    print("({}) Word's Prefix With ({})".format(count,pref))

words = [ word for word in input("Enter Words Separated with Space: ").split()]
pref = input("Enter Prefix Word: ")

print("-"*52)
prefixCount(words,pref)
print("-"*52)