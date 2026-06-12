# 2309. Greatest English Letter in Upper and Lower Case

def greatestLetter(s):
    greater = ""
    st = set(s)
    for ch in st:
        if ch.isupper() and ch.lower() in st:
            if ch > greater:
                greater = ch
    return greater
    

s = input("Enter any string: ")
res = greatestLetter(s)
print("~"*30)
print("Greatest Letter:",res)
print("~"*30)