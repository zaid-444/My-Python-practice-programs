# 2951. Find the Peaks

def findPeaks(mountain):
    lst = []
    for i,v in enumerate(mountain):
        if i == 0 or i == len(mountain)-1:
            continue
        else:
            if v > mountain[i-1] and v > mountain[i+1]:
                lst.append(i)
    return lst

mountain = [ int(num) for num in input("Enter mountain: ").split() ]
print("~"*30)
print("Output:",findPeaks(mountain))
print("~"*30)