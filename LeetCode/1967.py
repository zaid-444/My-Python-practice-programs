# 1967. Number of Strings That Appear as Substrings in Word

def numOfStrings(patterns,word):
    for w in patterns:
        if w in word:
            c += 1
    return c

patterns = ["a","abc","bc","d"]
word = "abc"
print(numOfStrings(patterns,word))