# 7. Reverse Integer

def reverse(x):
    if x >= 0:
        temp = int(str(x)[::-1])
    else:
        temp = -int(str(x)[len(str(x))-1:0:-1])
    if -2147483648 <= temp <= 2147483647:
        return temp
    return 0

x = int(input("> "))
print("~"*20)
print(f"Output: {reverse(x)}")
print("~"*20)