# Write a python program which will accept list of numerical values and find there sum and avg by using function's

def readvalues():
    print("Enter List of Values and press any special symbol to stop")
    lst = list()
    while True:
        val = input()
        if val.isalnum() or val.__contains__(".") or val.startswith("-"):
            lst.append(val)
        else:
            break
    return lst


def calsumavg(res):
    if len(res) == 0:
        print("List is Empty Sum and Avg Can't Calculate")
    else:
        s = 0
        for val in res:
            s = float(val) + s
        else:
            print("-"*50)
            print("Sum of Values = {}".format(s))
            print("Avg of Values = {:.2f}".format(s/len(res)))
            print("-"*50)

res = readvalues()
calsumavg(res)