# 3. Write a Python program to get the largest number from a list.

lst = [125,56,14,-856,54,68,654]

lg = lst[0]

for i in lst:
    if lg < i:
        lg = i

print("-"*50)
print("From this list =",lst)
print("Largest number =",lg)
print("-"*50)