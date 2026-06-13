# 2278. Percentage of Letter in String

def percentageLetter(s,letter):
    return int(s.count(letter)/len(s)*100)

s = input("Enter a String: ")
letter = input("Enter a char: ")

res = percentageLetter(s,letter)
print("~"*20)
print("Result:",res)
print("~"*20)