# 3120. Count the Number of Special Characters

def numOfSpec(word):
    st = set(word)
    c = 0
    for s in st:
        if s.islower() and s.upper() in st:
            c += 1
    return c


word = input("Enter any thing: ")
res = numOfSpec(word)
print("-"*30)
print("Output:",res)
print("-"*30)