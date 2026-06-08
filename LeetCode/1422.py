# 1422. Maximum Score After Splitting a String

def maxScore(s):
    mx = 0
    for i in range(1,len(s)):
        right = s[i:]
        left = s[:i]
        c = right.count("1") + left.count("0")
        if mx < c:
            mx = c
    return mx


s = input("Enter string: ")
print("-"*40)
print("Output:",maxScore(s))
print("-"*40)