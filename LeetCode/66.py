# 66. Plus One

def plusOne(digits):
    n = len(digits)
    for i in range(n-1,-1,-1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


digits = [ int(i) for i in input("> ").split() ]
print("~"*20)
print(f"Output: {plusOne(digits)}")
print("~"*20)