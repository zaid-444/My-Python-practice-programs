# Write a python programe which will accept any word and check weather it is palindrome or not

word = input("Enter a value: ")

res = "({}) is Palindrome".format(word) if word == word[::-1] else "({}) is not Palindrome".format(word)

print(res)