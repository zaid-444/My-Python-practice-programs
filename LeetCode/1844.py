# 1844. Replace All Digits with Characters

def replaceDigits(s):
    new = ""
    for i in range(len(s)):
        if i%2 == 1:
            num_int = int(s[i])
            chr_num = ord(s[i-1])
            new += chr(num_int+chr_num)
        else:
            new += s[i]
    print("After Replacing:",new)

s = input("Enter chr and digits: ")
print("-"*40)
print("Before Replacing:",s)
replaceDigits(s)
print("-"*40)