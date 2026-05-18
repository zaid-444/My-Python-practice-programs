# 2828. Check if a String Is an Acronym of Words

def isAcronym(words,s):
    l = []
    w = ""
    for word in words:
        l.append(word[0])
    return True if w.join(l) == s else False

words = [ val for val in input("Enter Words: ").split() ]
s = input("Enter value of S: ")

print("-"*30)
print("IsAcronym:",isAcronym(words,s))