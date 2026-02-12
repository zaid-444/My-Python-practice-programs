# write a python program which will aceept list of words into two types of list object and concatinate two list object using -

print("Enter 1st list words")
word1 = [val for val in input().split() ]
print("Enter 2nd list words")
word2 = [ val for val in input().split() ]

con = list(map(lambda w1,w2: w1+'-'+w2,word1,word2))

print("="*50)
print("Word1\t\tWord2\t\tCon Word")
print("="*50)
for w1,w2,c in zip(word1,word2,con):
    print("{}\t\t{}\t\t{}".format(w1,w2,c))

print("="*50)