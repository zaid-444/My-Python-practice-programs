# Write a python program which will validate mobile number by using regulare expressions

import re

while True:
    number = input("Enter any Mobile no.: ")
    if len(number) == 10:
        res = re.match(r"\d{10}",number)
        if res != None:
            print("{} :is Valid Mobile Number".format(number))
            break
        else:
            print("{} :Mobile number me tere baap ne alphabates dala tha?".format(number))
    else:
        print("{} :Is Invalid Mobile Number plz-try again".format(number))