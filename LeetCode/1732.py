# 1732. Find the Highest Altitude

def largestAltitude(gain):
    crrnt = 0
    mx = 0
    for i in gain:
        crrnt += i
        if crrnt > mx:
            mx = crrnt
    return mx


gain = [ int(i) for i in input("> ").split() ]
print("~"*30)
print("Output:",largestAltitude(gain))
print("~"*30)