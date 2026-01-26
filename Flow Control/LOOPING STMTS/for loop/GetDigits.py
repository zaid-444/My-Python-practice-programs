# Write a python program which will accept line of text and obtain only digits where a line of text contains alphabates digits and special symbols

s = input("Enter anything to get from this only digits: ")

count = 0

for i in s:
    if i.isdigit():
        print(i,end=' ')
        count += 1

print('Count of Digits = ',count)