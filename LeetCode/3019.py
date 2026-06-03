# 3019. Number of Changing keys

def countKeyChngs(s):
    c = 0
    for i in range(len(s)-1):
        if s[i].lower() != s[i+1].lower():
            c += 1
    print("Number of Changed Keys:",c)

s = input("Enter any String: ")
print("------------------------------")
countKeyChngs(s)
print("------------------------------")