# 2000. Reverse Prefix of Word

def reversePrefix(word,ch):
    lst = list(word)
    if ch in word:
        indx = lst.index(ch)
        rstr = lst[indx::-1]
        rstr += lst[indx+1::]
        return "".join(rstr)
    return word


word = input("Enter any word: ")
ch = input("Enter any Charachter: ")

print("~"*30)
print("After Reversing:",reversePrefix(word,ch))
print("~"*30)
