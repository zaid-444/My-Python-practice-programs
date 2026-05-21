# 1859. Sorting the Sentence

def sortSentence(s):
    lst = s.split()
    res = s.split()
    for word in lst:
        indx = int(word[-1]) - 1
        res[indx] = word[:-1]
    print("Before Sorting Sentence:",s)
    print("After Sorting Sentence: "," ".join(res))


sentence = input("Enter any sentence: ")
print("-"*50)
sortSentence(sentence)
print("-"*50)