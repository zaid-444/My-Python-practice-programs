# 1189. Maximum Number of Ballons

def func(text):
    d = {}
    for ch in text:
        d[ch] = d.get(ch,0)+1
    b = d.get("b",0)
    a = d.get("a",0)
    l = d.get("l",0) // 2
    o = d.get("o",0) // 2
    n = d.get("n",0)
    return min(b,a,l,o,n)

text = input("Enter a string: ")
print("~"*20)
print("Output:",func(text))
print("~"*20)