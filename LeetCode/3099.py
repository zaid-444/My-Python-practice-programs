# 3099. Harshad Number

def harshadNumber(x):
    s = 0
    for d in str(x):
        s += int(d)
    if x%s == 0:
        return s
    else:
        return -1
    
res = harshadNumber(int(input("Enter any Number: ")))
print("Output:",res)

# 2255