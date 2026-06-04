# 1941. Check if All Characters Have Equal Number of Occurrences

def occurEqual(s):
    n = s.count(s[0])
    for i in s:
        if s.count(i) != n:
            return False
    return True


s = input("Enter any String: ")
res = occurEqual(s)
print("~"*30)
print("Result:",res)
print("~"*30)