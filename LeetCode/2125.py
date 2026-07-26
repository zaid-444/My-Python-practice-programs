# 2125. Number of Laser Beams in a Bank

def numberOfBeams(bank):
    prev = 0
    result = 0
    for row in bank:
        curr = 0
        for ch in row:
            if ch == "1":
                curr += 1
        if curr:
            result += prev*curr
            prev = curr
    return result


bank = ["011001","000000","010100","001000"]
print("~"*20)
print(f"Output: {numberOfBeams(bank)}")
print("~"*20)