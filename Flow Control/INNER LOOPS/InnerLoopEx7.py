# Write a python program which will accept list of numerical values and display Mul table for those numbers

nov = int(input("Enter how many values u want to enter: "))

if nov <= 0:
    print(f'{nov} is Invalid Input')
else:
    lst = list()
    for i in range(1,nov+1):
        mul = int(input(f'Enter val no.{i}: '))
        lst.append(mul)
    else:
        print("-"*30)
        print(lst)
        print("-"*30)
        for num in lst:
            if num <= 0:
                print(f'For {num} Mul Table not Exist')
                print("-"*30)
            else:
                for i in range(1,11):
                    print(f'{num} x {i} = {num*i}')
                else:
                    print("-"*30)