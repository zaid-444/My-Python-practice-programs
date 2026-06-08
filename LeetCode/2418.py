# 2418. Sort the People

def sortPeople(names,heights):
    zipp = list(zip(heights,names))
    zipp.sort(reverse=True)
    lst = []
    for ht,nm in zipp:
        lst.append(nm)
    return lst

names = ["Mary","John","Emma"]
heights = [180,165,170]

print("-"*40)
print("Output:",sortPeople(names,heights))
print("-"*40)