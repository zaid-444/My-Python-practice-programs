# 2833. Furthest Point From Origin

def furthDist(moves):
    L = moves.count("L")
    R = moves.count("R")
    _ = moves.count("_")
    if L > R:
        L += _
        return L-R
    else:
        R += _
        return R-L
    
moves = input("Enter Your Moves From (LR_) only: ").upper()

res = furthDist(moves)
print("~"*20)
print("Output:",res)
print("~"*20)