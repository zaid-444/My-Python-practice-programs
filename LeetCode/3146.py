# 3146. Permutation Difference between Two Strings

def findPerDiff(s,t):
    total = 0
    l = list(t)
    for i in range(len(s)):
        indx = l.index(s[i])
        if i > indx:
            total += i - indx
        else:
            total += indx - i
    print(f'Output: {total}')

s = input("Enter 1st String: ")
t = input("Enter 2nd String: ")

print("------------------------")
findPerDiff(s,t)
print("------------------------")