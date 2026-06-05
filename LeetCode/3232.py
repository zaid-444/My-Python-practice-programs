# 3232. Find if Digit Game Can Be Won

def canAliceWin(nums):
    single = 0
    double = 0
    for n in nums:
        if n < 10:
            single += n
        else:
            double += n
    return single != double


nums = [ int(i) for i in input("Enter Numbers: ").split() ]
print("~"*30)
print("canAliceWin:",canAliceWin(nums))
print("~"*30)