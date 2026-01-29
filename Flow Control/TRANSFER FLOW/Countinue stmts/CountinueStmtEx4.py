# Write a python program which will accept list of word from keyboard and display those word's whose length either 3 or 5

nov = int(input("how many words you want to enter: "))

if nov <= 0:
    print("{} Invalid Input".format(nov))
else:
    lst = []
    for i in range(1,nov+1):
        word = input("Enter word {}: ".format(i))
        lst.append(word)
    else:
        print("List of word = {}".format(lst))

        word35 = list()
        for word in lst:
            if len(word) not in [3,5]:
                continue
            word35.append(word)
        else:
            print("3 and 5 length words are = {}".format(word35))