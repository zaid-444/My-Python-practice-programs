# 1528. Shuffle String

def restroreString(s,indices):
    lst = list(s)
    for i in range(len(s)):
        lst.insert(indices[i],s[i])
        lst.pop(indices[i]+1)
    return "".join(lst)

print("-"*50)
s = input("Enter a String: ")
print("Enter List of Indices Separated by Space")
indices = [ int(i) for i in input().split() ]
print("-"*50)

res = restroreString(s,indices)
print(f'Before the Shuffle: {s}')
print(f'After the Shuffle:  {res}')
print("-"*50)