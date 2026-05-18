# 3110. Score of a String

def scoreOfString(s):
    total = 0
    for i in range(len(s) - 1):
        a = ord(s[i])
        b = ord(s[i+1])
        if a > b:
            total += a - b
        else:
            total += b - a
    return total


s = input("Enter a String: ").lower()
print("-"*50)
res = scoreOfString(s)
print("Score of a String =",res)
print("-"*50)
