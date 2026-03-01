# 11. Write a Python function that takes two lists and returns True if they have at least one common member

def fun(list1,list2):
    for i in list1:
        # for j in list2:
        #     if i == j:
        #         return True
        if i in list2:
            return True
    else:
        return False



lst1 = [ val for val in input("Enster List1 Ele: ").split() ]
lst2 = [ val for val in input("Enster List2 Ele: ").split() ]

res = fun(lst1,lst2)

print(res)