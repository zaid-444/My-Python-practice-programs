# Program for Demonstrating break key word

s = "PYTHON"
print("By using While Loop")

i = 0

while i < len(s):
    print(s[i])
    i = i + 1

print("-"*40)

# Requirment is to display 'PYTH'

i = 0

while i < len(s):
    if s[i] == "O":
        break
    print(s[i],end='')
    i += 1
else:
    print("Im am else part of for loop")

print("\nOther statements in Program")