def isValid(s):
    l = []
    for b in s:
        if b == "(" or b == "[" or b == "{":
            l.append(b)
        else:
            if len(l) == 0:
                return "{} this is not Valid Parentheses".format(s)
            lb = l.pop()
            if b == ")" and lb == "(" or b == "]" and lb == "[" or b == "}" and lb == "{":
                continue
            else:
                return "{} this is not Valid Parentheses".format(s)
    if len(l) == 0:
        return "{} this is Valid Parentheses".format(s)
    else:
        return "{} this is not Valid Parentheses".format(s)

while True:
    print("-"*50)
    par = input("Enter any type of Paren: ")
    res = isValid(par)
    print("-"*50)
    print(res)
    print("-"*50)
    k = input("Do u want to try again yes/no: ")
    if k.lower() == "no":
        print("Thank you for using this program")
        break