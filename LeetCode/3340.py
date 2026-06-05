# 3340. Check Balanced String

def isBalanced(num):
    even = 0
    odd = 0
    for i in range(len(num)):
        if i%2 == 0:
            even += int(num[i])
        else:
            odd += int(num[i])
    return even == odd

num = input("Enter number: ")
print("~"*30)
print(f"{num} isBalanced: {isBalanced(num)}")
print("~"*30)