# 520. Detect Capital

def detectCapitalUse(word):
    if word.islower():
        return True
    elif word.isupper():
        return True
    elif word[0].isupper() and ("".join(word[1:]).islower()):
        return True
    else:
        return False
    
word = input("> ")
print("~"*15)
print(f"Output: {detectCapitalUse(word)}")
print("~"*15)