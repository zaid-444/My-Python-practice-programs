# Write a python program which will accept a line of text and obtains speacial symbols where a line of text contains alphabates digits and special symbols

print("-"*50)

s = input("Enter any thing to get only specail chr: ")

print("-"*50)

count = 0

for ch in s:
    if not ch.isalnum():        
        print(ch,end=' ')
        count += 1

print(f'\nCount of Specail Symbols are = {count}')
print("-"*50)