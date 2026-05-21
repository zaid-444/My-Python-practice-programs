# 2255. Count Prefixes of a Given String

def countPrefixes(words,s):
    count = 0
    for word in words:
        if s.startswith(word):
            count += 1
    print("Output:",count)

words = [ val for val in input("Enter string: ").split() ]
s = input("Enter s: ")

print("-"*50)
countPrefixes(words,s)
print("-"*50)