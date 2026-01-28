# Program for Demonstrating break key word

s = "PYTHON"
print("By using For Loop")

for ch in s:
    print("\t{}".format(ch))
else:
    print("Im am else part of for loop")

print("-"*40)

# Requirment is to display 'PYTH' without using Indexing and Slicing

for ch in s:
    if ch == "O":
        break
    else:
        print(ch,end="")
else:
    print("Im am else part of for loop")

print("\nOther statements in Program")