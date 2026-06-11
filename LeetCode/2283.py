# 2283. Check if Number Has Equal Digit Count and Digit Value

def digitCount(num):
    for i in range(len(num)):
        if num.count(str(i)) != int(num[i]):
            return False
    return True


num = input("Enter number: ")
print("~"*20)
print("digitCount:",digitCount(num))
print("~"*20)