list1 = [1,2,4]
list2 = [1,3,4]

sortedLst = []

for i in range(len(list1)):
    sortedLst.append(list1[i])
for j in range(len(list2)):
    sortedLst.append(list2[i])
sortedLst.sort()
print(sortedLst)