# 1816. Truncate Sentence

def trunSen(s,k):
    lst1 = s.split()
    lst2 = []
    for i in range(k):
        lst2.append(lst1[i])
    return " ".join(lst2)

s = input("Enter any Sentence: ")
k = int(input("Enter value of K: "))
print("-"*40)
res = trunSen(s,k)
print("Output:",res)
print("-"*40)