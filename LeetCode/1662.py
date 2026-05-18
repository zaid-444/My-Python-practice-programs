# 1662. Check If Two String Arrays are Equivalent

def arrayStringsAreEqual(word1,word2):
    w1 = ""
    w2 = ""
    return w1.join(word1) == w2.join(word2)

word1 = [ word for word in input("Enter list of words1: ").split() ]
word2 = [ word for word in input("Enter list of words2: ").split() ]

print("-"*40)
res = arrayStringsAreEqual(word1,word2)
print("List Are Equal =",res)
print("-"*40)