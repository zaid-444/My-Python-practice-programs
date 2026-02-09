# Write a python program which will accept list words whose length is either two or four only, from list of words

print("-"*60)
word24 = [ word for word in input().split() if len(word) in [2,4] ]
print("Two and Four Len words =",word24)
print("-"*60)