# 2129. Capitalize the Title

def capitalizeTitle(title):
    lst = title.split()
    nlst = []
    for val in lst:
        if len(val) > 2:
            nlst.append(val.title())
        else:
            nlst.append(val.lower())
    return " ".join(nlst)


title = input("Enter String: ")
res = capitalizeTitle(title)
print("~"*50)
print("Output:",res)
print("~"*50)