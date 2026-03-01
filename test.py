l1 = int(input("Enter how many elements u want to add in Array 1: "))
arr1 = []
for i in range(1,l1+1):
    a = int(input("Enter elemnt no. {}: ".format(i)))
    arr1.append(a)


l2 = int(input("Enter how many elements u want to add in Array 2: "))
arr2 = list()

for i in range(1,l2+1):
    a = int(input("Enter elemnt no. {}: ".format(i)))
    arr2.append(a)

small = min(l1,l2)

arr3 = []

a = 0
while a < small:
        if l1 >= l2:
            arr3.append(arr1[a])
            arr3.append(arr2[a])
        else:
            arr3.append(arr2[a])
            arr3.append(arr1[a])
        a += 1

print("Array 1 =",arr1)
print("Array 2 =",arr2)
print("Array 3 =",arr3)