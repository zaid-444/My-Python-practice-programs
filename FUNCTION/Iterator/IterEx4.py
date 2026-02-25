# Program for demonstrating Iterator

dct = {10:"Zaid",20:"Rohit",30:"Virat",40:"Ishan",50:"Dhoni"}

iterobj = iter(dct)

for key in iterobj:
    print("{} ==> {}".format(key,dct[key]))