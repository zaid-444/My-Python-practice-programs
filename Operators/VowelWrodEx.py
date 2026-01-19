# Program for accepting a word a Decide whether It is Vowel Word or not

word = input("Enter any word: ")

res = "{} is Vowel Word".format(word) if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word else "{} is Not Vowel Word".format(word)

print(res)

