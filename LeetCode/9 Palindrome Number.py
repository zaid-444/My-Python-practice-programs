def isPalindrome(x):
    return str(x) == str(x)[::-1]

res1 = isPalindrome(123)
res2 = isPalindrome(121)
print(res1)
print(res2)