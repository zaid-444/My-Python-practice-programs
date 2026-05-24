# 3168. Minimum Nunber of Chairs in a Waiting Room

def minChairs(s):
    chair = 0
    lst = []
    for p in s:
        if p == "E":
            chair += 1
            lst.append(chair)
        else:
            chair -= 1
            lst.append(chair)
    
    return max(lst)

s = input("Enter Events: ")

res = minChairs(s)
print("-"*50)
print("Output:",res)
print("-"*50)