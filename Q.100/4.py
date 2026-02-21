# 4. Write a Python program to get the smallest number from a list.

lst = [65,-88,-54,665,65,2,64,78]

sm = lst[0]

for i in lst:
    if i < sm:
        sm = i

print("List  =",lst)
print("Small =",sm)