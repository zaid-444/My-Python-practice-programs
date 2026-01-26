# Write a python program which will accept a line of text and obtains speacial symbols where a line of text contains alphabates digits and don't include spaces

print("-"*50)
s = input("Enter any thing: ")
print("-"*50)

count = 0

for ch in s:
    if not ch.isalnum() and not ch.isspace():
        print(ch)
        count += 1
print("-"*50)
print('Count of Specail Symbols = ',count)
print("-"*50)