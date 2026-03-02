# Write a python program which will read the data continuously from the keyboard and write it to the file

print("Enter Your Info. and stop using @")

with open("info.data","a") as fp:
    while True:
        data = input()
        if data != "@":
            fp.write(data+"\n")
        else:
            print("-"*50)
            print("Information Taken")
            break