# Program for check Work Day or Holiday or Week-end-Day

wkd = input("Enter The Day Name: ").upper()

match wkd:
    case "MONDAY":
        print("{} is Work Day".format(wkd))
    case "TUESDAY":
        print("{} is Work Day".format(wkd))
    case "WEDNESDAY":
        print("{} is Work Day".format(wkd))
    case "THURSDAY":
        print("{} is Work Day".format(wkd))
    case "FRIDAY":
        print("{} is work Day".format(wkd))
    case "SATURDAY":
        print("{} is Week-End Day".format(wkd))
    case "SUNDAY":
        print("{} is Holiday".format(wkd))
    case _:
        print("{} is not Any Day Name".format(wkd))