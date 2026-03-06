# Write a python program which will remove folders hierarchy

import os

try:
    os.removedirs("INDIA\\MH\\PUNE\\PYTHON")
    print("Folders Deleted")
except FileNotFoundError:
    print("Folders not exist")