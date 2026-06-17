# 2315. Count Asterisks

def countAsterisks(s):
    count = 0
    a = 0
    for ch in s:
        if ch == "|":
            a += 1
        elif a%2 == 0 and ch == "*":
            count += 1
    return count


s = "l|*e*et|c**o|*de|"

print("~"*30)
print(f"Total Asterisks: {countAsterisks(s)}")
print("~"*30)