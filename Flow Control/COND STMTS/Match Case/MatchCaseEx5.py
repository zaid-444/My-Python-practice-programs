wkd = input("Enter the week Day name: ").upper()

if wkd in ["MON","TUE","WED","THU","FRI","SAT","SUN","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]:
    match wkd[:3]:
        case "MON"|"TUE"|"WED"|"THU"|"FRI":
            print("{} is working Day".format(wkd))
        case "SAT":
            print("{} is week-end".format(wkd))
        case "SUN":
            print("{} is holiday day".format(wkd))
else:
    print("{} is not week day".format(wkd))