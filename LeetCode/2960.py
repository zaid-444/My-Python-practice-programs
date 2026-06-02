# 2960. Count Tested Devices After Test Operations

def countTestedDevices(battery):
    opr = 0
    for i in range(len(battery)):
        if battery[i] > 0:
            opr += 1
            for j in range(i,len(battery)):
                if battery[j] > 0:
                    battery[j] = battery[j]-1
    return opr



battery = [ int(num) for num in input("Enter batteryPercentages: ").split() ]
print("Operations =",countTestedDevices(battery))