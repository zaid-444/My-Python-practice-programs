# Write a python program which will accept list of words and find highest length words 

def getword():
    print("Enter word and press @ to Stop")
    lst = []
    while True:
        word = input("Enter word: ")
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
        for val in words:
            d[val] = len(val)
        else:
            lst = []
            print(d)
            ml = max(d.values())
            for word,length in d.items():
                if length == ml:
                    lst.append(word)
            else:
                print("Max Length Words")
                for word in lst:
                    print("\t{}".format(word))
                else:
                    print("Number of Max length Words = ",len(lst))               
                         
words = getword()
findmaxlenword(words)