# 2108. Find First Palindromic String in the Array

def firstPalindrome(words):
    temp = ""
    for word in words:
        if word == word[::-1]:
            temp = word
            break
    return temp

words = [ val for val in input("Enter Words: ").split() ]

print("-"*50)
res = firstPalindrome(words)
if res:
    print("The First Palindrome is:",res)
else:
    print("There is no Palindrome")
print("-"*50)