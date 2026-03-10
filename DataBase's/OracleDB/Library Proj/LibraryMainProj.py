from LibraryMenu import menu
from LibraryAdd import addbook

while True:
    try:
        menu()
        choice = int(input("Enter Your Choice: "))
        match choice:
            case 1: 
                addbook()
            case 2: pass
            case 3: pass
            case 4: pass
            case 5: pass
            case 6:
                print("Thxx For Using Our Application...")
                break
            case _:
                print("-"*41)
                print("This Operation Not Available yet!!!")
    except ValueError:
        print("-"*41)
        print("Enter only numbers...")