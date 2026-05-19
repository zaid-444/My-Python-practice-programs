# 1342. Number of Steps to Reduce a Number to Zero

def numberOfSteps(num):
    count = 0
    while num != 0:
        if num%2 == 0:
            num /= 2
            count += 1
        else:
            num -= 1
            count += 1
    return count

num = int(input("Enter Any Number: "))
print("-"*50)
res = numberOfSteps(num)
print("Number of Steps to Reduce ({}) to Zero: {}".format(num,res))
print("-"*50)