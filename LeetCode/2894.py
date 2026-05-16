# 2894. Divisible and Non-divisible Sums Difference

def difSums(n,m):
    num1 = 0
    num2 = 0
    for i in range(1,n+1):
        if i%m != 0:
            num1 += i
        else:
            num2 += i
    print("Difference Between {} - {} = {}".format(num1,num2,num1-num2))

n = int(input("Enter Value of N: "))
m = int(input("Enter Value of M: "))

print("-"*50)
difSums(n,m)
print("-"*50)
