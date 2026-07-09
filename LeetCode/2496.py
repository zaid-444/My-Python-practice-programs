# 2496. Maximum Value of a String in an Array

def maximumValue(strs):
    mx = 0
    for ch in strs:
        if ch.isdigit():
            mx = max(mx,int(ch))
        else:
            mx = max(mx,len(ch))
    return mx


strs = [ i for i in input("> ").split() ]
print("~"*20)
print(f"Output: {maximumValue(strs)}")
print("~"*20)