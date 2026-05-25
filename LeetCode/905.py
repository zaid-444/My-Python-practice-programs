# 905. Sort Array By Parity

def sortArray(nums):
    odd = []
    even = []
    for num in nums:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even+odd

nums = [ int(num) for num in input("Enter Numbers: ").split() ]
print("Output:",sortArray(nums))