# Write a python program which will count number of lines number of words and number of charachters in a given file

try:
    filename = input("Enter any File Name: ")
    with open(filename,"r") as fp:
        filedata = fp.readlines()
        nl,nw,nc = 0,0,0
        for line in filedata:
            nl += 1
            nw = nw + len(line.split())
            nc = nc + len(line)
        print("No. of lines =",nl)
        print("No. of Words =",nw)
        print("No. of Chars =",nc)
        
except FileNotFoundError:
    print("File Not Exist")