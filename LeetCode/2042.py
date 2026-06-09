# 2042. Check if Number Are Ascending in a Sentence


def areNumbersAscending(s):
    lst = []
    for val in s.split():
        if val.isdigit():
            if int(val) in lst:
                return False
            else:
                lst.append(int(val))
    copy_lst = lst.copy()
    copy_lst.sort()
    return lst == copy_lst


s = input("Enter Sentence: ")
res = areNumbersAscending(s)

print("-"*50)
print(f"areNumbersAscending: {res}")
print("-"*50)