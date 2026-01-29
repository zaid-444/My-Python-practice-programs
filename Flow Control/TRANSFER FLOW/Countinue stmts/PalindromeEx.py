# Write a python program which will accept list of words from keyboard and extract only palindrome word

print("Enter Number of Words and Press any special to stop")

lst = []
while True:
    word = input("Enter any word: ")
    if not word.isalnum():
        break
    lst.append(word)

print("List of Words = {}".format(lst))

plst = list()
for word in lst:
    if word != word[::-1]:
        continue
    plst.append(word)

print(plst)