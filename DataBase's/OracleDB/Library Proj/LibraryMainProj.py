from LibraryMenu import menu
from LibraryAdd import addbook
from LibraryDelete import deletebook
from LibraryView import viewallbooks,viewbook
from LibraryUpdate import updatebook

while True:
    try:
        menu()
        choice = int(input("Enter Your Choice: "))
        match choice:
            case 1: 
                addbook()
            case 2: 
                deletebook()
            case 3: 
                updatebook()
            case 4: 
                viewbook()
            case 5: 
                viewallbooks()
            case 6:
                print("Thxx For Using Our Application...")
                break
            case _:
                print("-"*41)
                print("This Operation Not Available yet!!!")
    except ValueError:
        print("-"*41)
        print("Enter only numbers...")