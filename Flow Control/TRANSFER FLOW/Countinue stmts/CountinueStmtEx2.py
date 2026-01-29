# Program for Demonstrating Continue Statement

s = "PYTHON"

i = 0

while i < len(s):
    print(s[i])
    i += 1
else:
    print("else part of while loop")

print("-------------------------------------")

# Requirement is to display: PYON
i = 0

while i < len(s):
    if s[i] in ["T", "H"]:
        i += 1
        continue
    print(s[i],end="")
    i += 1
else:
    print("\nelse part of while loop")

print("-------------------------------------")