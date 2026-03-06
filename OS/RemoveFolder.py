# Program for Removing a Folder

import os
try:
    os.rmdir("Zaid\\Sunny\\Katrina")
    print("Folder Deleted")
except FileNotFoundError:
    print("Folder not Exist")
except OSError:
    print("Folder not empty")