# Program for Demonstrating Continue Statement

s = "PYTHON"

for ch in s:
    print(ch)
else:
    print("else part of for loop")

print("-------------------------------------")

# Requirement is to display: PYTON

for ch in s:
    if ch == "H":
        continue
    print(ch,end="")
else:
    print("\nelse part of for loop")

print("-------------------------------------")