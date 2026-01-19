# Write a python program which will accept any word and decide whether it is Consonants

word = input("Enter any Word: ")

res = "{}: is Consonants".format(word) if 'a' not in word and 'e' not in word and 'i' not in word and 'o' not in word and 'u' not in word else "{}: is not Consonants".format(word)

print(res)