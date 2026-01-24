wkd = input("Enter the Day Name: ").upper()

match wkd[:3]:
    case "MON"|"TUE"|"WED"|"THU"|"FRI":
        print("{} is Work Day".format(wkd))
    case "SAT":
        print("{} is Week-End".format(wkd))
    case "SUN":
        print("{} is Holiday Day".format(wkd))
    case _:
        print("{} is not week Day".format(wkd))