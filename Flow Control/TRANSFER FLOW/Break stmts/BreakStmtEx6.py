# Write a python program which will accept a word and seperate upper case letters, lower case letter, digits and special symbols

s = input("Enter anything: ")
ul = ''
ll = ''
d = ''
ss = ''

for i in s:
    if i.isupper():
        ul += i
    elif i.islower():
        ll += i
    elif i.isdigit():
        d += i
    else:
        ss += i

print("-"*40)

print(f"UPPER LETTER      : {ul}")
print(f"LOWER LETTER      : {ll}")
print(f"DIGITS            : {d}")
print(f"SPECIAL SYMBOLS   : {ss}")

print("-"*40)