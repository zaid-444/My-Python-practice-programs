# Write a python program which will accept a word or line of text and display each and every char

wl = input("Enter Any word or line: ")

i = 0
while i < len(wl):
    print(wl[i])
    i += 1

print("-"*5)

i = len(wl)-1
while 0 <= i:
    print(wl[i])
    i -= 1

print("-"*5)

i = 0
wl = wl[::-1]
while i < len(wl):
    print(wl[i])
    i += 1

print("-"*5)

wl = wl[::-1]
i = -1
while i >= -(len(wl)):
    print(wl[i])
    i -= 1