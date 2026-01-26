# Write a python program which will accept line of text or word and obtain only alphabates where line of text contains combination of alphabates digits and speacial symbols

s = input("Enter word or line to get only alphabates: ")

for ch in s:
    if ch.isalpha():
        print(ch,end=' ')

print(f'\n{"-"*50}')
print("Another Method")
print("-"*50)

s = input("Enter word or line to get only alphabates: ")

i = 0

while i < len(s):
    if s[i].isalpha():
        print(s[i],end=' ')
    i += 1