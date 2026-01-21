# HW. Write a python Program which will accept any word and decide it is palindrome or not by using simple if statemante

word = input("Enter any Word: ")

if word == word[::-1]:
    print("{} is Palindrome word".format(word))

if word != word[::-1]:
    print("{} is Not Palindrome word".format(word))