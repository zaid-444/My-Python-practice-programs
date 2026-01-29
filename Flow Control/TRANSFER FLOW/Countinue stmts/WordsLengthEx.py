# Write a python program which will accept line of text and find length of each word

text = input("Enter line of text: ")

print("Given words = {}".format(text))

lst = text.split()

print("-"*40)
for word in lst:
    print("{}-----> {}".format(word,len(word)))
print("-"*40)

wdict = dict()

for word in lst:
    wdict[word] = len(word)
else:
    for k,v in wdict.items():
        print("{}----> {}".format(k,v))

print("------------------------or-----------------------")

wt = list()

for word in lst:
    wt.append((word,len(word)))
else:
    for tpl in wt:
        print(tpl)