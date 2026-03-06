# Program for renaming the folder

import os

try:
    os.rename("Zaids","Raahi")
    print("Folder name Changed Successfully")
except FileNotFoundError:
    print("Filde not Exist")