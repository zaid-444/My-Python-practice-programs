# 2490. Circular Sentence

def xyz(sentence):
    lst = sentence.split()
    if lst[0][0] != lst[-1][-1]:
        return False
    for i in range(len(lst)-1):
        if lst[i][-1] != lst[i+1][0]:
            return False
    return True

sentence = input("Enter a Sentence: ")

res = xyz(sentence)

print("~"*20)
print("Output:",res)
print("~"*20)