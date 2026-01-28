#  Program for Demonstrating break key word

s = "MISSISSIPPI"
print("By using while loop")

i = 0
while i < len(s):
    print(s[i])
    i += 1

print("-"*30)

# Requirment is to display 'MISS' without using Indexing and slicing using while

ci = 0
i = 0

while i < len(s):
    if s[i] == "I":
        ci = ci + 1
        if ci == 2:
            break
    print(s[i],end='')
    i = i + 1
else:
    print("I am from else part of while loop")

print("\nOther statements in Program")