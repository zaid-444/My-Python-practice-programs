# 2942. Find Words Containing Character

def findWordsContaining(words,x):
    lst = list()
    for index,value in enumerate(words):
        if x in value:
            lst.append(index)
    print("Output =",lst)

print("-"*50)
print("Enter List Values Separated by Space")
words = [ i for i in input().split() ]
x = input("Enter Value of X: ")
print("-"*50)
findWordsContaining(words,x)
print("-"*50)