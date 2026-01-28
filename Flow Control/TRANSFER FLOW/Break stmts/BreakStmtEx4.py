#  Program for Demonstrating break key word

s = "MISSISSIPPI"
print("By using for loop")

for ch in s:
    print(ch)

print("-"*30)

# Requirment is to display 'MISS' without using Indexing and slicing

ci = 0

for ch in s:
    if ch == "I":
        ci = ci + 1
        if ci == 2:
            break
    print(ch,end='')
else:
    print("I am from else part of while loop")

print("\nOther statements in Program")