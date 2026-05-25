# 3184. Count Pairs That Form a Complete Day

def countComDay(hours):
    count = 0
    for i in range(len(hours)):
        for j in range(i+1,len(hours)):
            if (hours[i] + hours[j])%24 == 0:
                count += 1
    print("Complete Hours Pair:",count)

hours = [ int(hour) for hour in input("Enter Hours List: ").split() ]
print("~"*30)
countComDay(hours)
print("~"*30)
print("{}".format(hours))