# Write a python program which will implement the following
# Given Input lst = [123,45,24,89]
# Expected output [6,9,6,17] Find the sume of Digits of Each Number of List

inp = int(input("How many numbers you want to enter: "))

if inp <= 0:
    print(f'{inp} is invalid input')
else:
    lst = list()
    for i in range(1,inp+1):
        num = int(input("Enter Value no.{}: ".format(i)))
        lst.append(num)
    else:
        sum_lst = list()
        for i in lst:
            add = 0
            for j in str(i):
                add = add + int(j)
            else:
                sum_lst.append(add)

print("-"*50)
print("List of Values = {}".format(lst))
print("Sum of List Values = {}".format(sum_lst))
print("-"*50)