# 258. Add Digits

def addDigits(num):
    while num > 9:
        s = 0
        for n in str(num):
            s += int(n)
        num = s
    return num

print("Output:",addDigits(int(input("Enter any Number: "))))