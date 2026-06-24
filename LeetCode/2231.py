# 2231. Largest Number After Digit Swaps by Prity


def largestInt(num):
    evn = []
    odd = []
    for n in str(num):
        if int(n)%2 == 0:
            evn.append(n)
        else:
            odd.append(n)
    evn.sort()
    odd.sort()
    ans = ""
    for d in str(num):
        if int(d)%2 == 0:
            ans += evn.pop()
        else:
            ans += odd.pop()
    return int(ans)


num = int(input("Enter value of N: "))
print("~"*20)
print(f"Output: {largestInt(num)}")
print("~"*20)