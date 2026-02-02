# Write a python program which will accept list of words and find highest length words without max

def getword():
    print("-"*40)
    print("Enter word and press @ to Stop")
    lst = []
    while True:
        word = input()
        if word == "@":
            break
        else:
            lst.append(word)
    return lst

def findmaxlenword(words):
    if len(words) == 0:
        print("There is no word to check")
    else:
       d = dict()
       for word in words:
           d[word] = len(word)
       else:
           lst = []
           print(d)
           val = list(d.values())
           ml = val[0]
           for i in val:
               if i > ml:
                   ml = i
           else:
               for wor,lenght in d.items():
                   if ml == lenght:
                       lst.append(wor)
               else:
                   print("*"*50)
                   print("Max Length Words")
                   for j in lst:
                       print("\t{}".format(j))
                   else:
                       print("Number of Max Length words = {}".format(len(lst)))
                   

lst = getword()
findmaxlenword(lst)