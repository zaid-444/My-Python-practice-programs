# Write a python program which will accept a word and decide whether it is Vowel word or not

word = input("Enter word to check Vowel or Not: ")

for i in word:
    if i.lower() in "aeiou":
        print("{} is Vowel Word".format(word))
        break
else:
    print("{} is Not Vowel word".format(word))