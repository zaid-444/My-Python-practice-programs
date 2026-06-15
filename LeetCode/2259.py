# 2259. Remove Digit From Number to Maximize Result

def removeDigit(number,digit):
    lst = []
    for i in range(len(number)):
        if number[i] == digit:
            lst.append(number[:i]+number[i+1:])
    return max(lst)


number = input("> ")
digit = input("> ")
res = removeDigit(number,digit)
print("~"*30)
print("Output:",res)
print("~"*30)