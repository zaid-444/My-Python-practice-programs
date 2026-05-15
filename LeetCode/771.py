# 771. Jewels and Stones

def numJewelsInStones(stn,jws):
    sc = 0
    for s in stn:
        if s in jws:
            sc += 1
    return sc

print("-"*50)
stn = input("Enter Stones: ")
jws = input("Enter Jewels: ")
print("-"*50)
res = numJewelsInStones(stn,jws)
print("Your Jewels Stone =",res)
print("-"*50)