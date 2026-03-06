# Write a python program which will list the files present in a folder

import os

try:
    FilesList = os.listdir("D:\WhatsApp")
    print("="*50)
    print("Number of Files =",len(FilesList))
    print("="*50)
    print("\tList of Files")
    print("="*50)
    for i in FilesList:
        print("\t{}".format(i))
    print("="*50)
    
except FileNotFoundError:
    print("Folder Does not exist")