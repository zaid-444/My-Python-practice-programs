# 2068. Check Whether Two Strings are Almost Equivalent

def func(word1,word2):
    d1 = {}
    d2 = {}
    for ch in word1:
        d1[ch] = d1.get(ch,0) + 1
    for ch in word1:
        d1[ch] = d1.get(ch,0) + 1

    words = set(word1 + word2)
    for ch in words:
        diff = abs(d1.get(ch,0) - d2.get(ch,0))
        if diff > 3:
            return False
    return True

word1 = input("Enter Word1: ")
word2 = input("Enter word2: ")
print("~"*15)
print("Output:",func(word1,word2))
print("~"*15)