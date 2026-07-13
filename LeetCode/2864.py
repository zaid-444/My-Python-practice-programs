# 2864. Maximum Odd Binary Number

def maximumOddBinaryNumber(s):
    ones = s.count("1")
    zeros = len(s) - ones
    return "1" * (ones-1) + "0"*zeros + "1"

s = input("> ")
print("~"*20)
print("Output:",maximumOddBinaryNumber(s))
print("~"*20)