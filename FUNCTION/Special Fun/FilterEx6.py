# Write a python program which will accept list of words and filter those words which are containing atleast one vowel

print("Enter list of Values separated by space")

lst = [ word for word in input().split() ]

voword = list(filter(lambda word: 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word,lst))
print("-"*50)
print("List of word's =",lst)
print("List of Vowel Word's =",voword)
print("-"*50)