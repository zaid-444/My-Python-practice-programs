# 2651. Calculate Delayed Arrival Time

def findDelArrTime(arrival,delay):
    total = arrival + delay
    if total < 24:
        return total
    else:
        return total - 24
    
arrival = int(input("Enter Arrival Time: "))
delay = int(input("Enter Delayed Time: "))

print("-"*50)
res = findDelArrTime(arrival,delay)
print("Arrival Time of the Train {}:00".format(res))
print("-"*50)