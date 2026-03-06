# Write a python program which will list the python files present in a folder

import os

try:
    foldername = input("Enter a Folder Path: ")
    FilesList = os.listdir(foldername)
    print("="*50)
    print("All Files =",len(FilesList))
    print("="*50)
    pc = 0
    for i in FilesList:
        # if i[-3:] == ".py":
        if i.endswith(".py"):
            pc += 1
    print("\tNumber of python files =",pc)
    print("="*50)
    
except FileNotFoundError:
    print("Folder Does not exist")