# Write a python prgram which will accept a Number and check whether it is palindrome or not

palindrome = lambda number: "Palindrome" if str(number) == str(number)[::-1] else "Not Palindrome"

number = int(input("Enter any number: "))

res = palindrome(number)

print("-"*50)
print("{} is {}".format(number,res))
print("-"*50)