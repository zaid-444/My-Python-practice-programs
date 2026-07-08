# 3754. Concatenate Non-Zero Digits and Multiply by Sum |

# Optimal TC--> O(d)   SC--> O(1)
def sumAndMultiply(n: int):
    x = 0
    s = 0
    for i in str(n):
        i = int(i)
        if i != 0:
            x = (x*10)+i
            s += i
    return x*s


print(f"Output: {sumAndMultiply(int(input("Enter n: ")))}")