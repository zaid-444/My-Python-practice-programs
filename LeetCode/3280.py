# 3280. Convert Date to Binary

def convDateToBin(date):
    l = date.split("-")
    l2 = []
    for i in l:
        x = bin(int(i))
        l2.append(x[2::])
    return "-".join(l2)

date = input("Enter Date: ")
print("~"*40)
print("Bin Date:",convDateToBin(date))
print("~"*40)