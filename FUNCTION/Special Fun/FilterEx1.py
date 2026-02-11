# Program for Filtering +VE and -VE Values from list of Values

def pos(val):
    if val > 0:
        return True
    else:
        return False

def neg(val):
    if val < 0:
        return True
    else:
        return False



lst = [10,-20,30,0,-66,52,0,-44,24]

ps = filter(pos,lst)
ns = filter(neg,lst)

psl = list(ps)
tns = tuple(ns)
print("List Data =",lst)
print("Possitve Values =",psl)
print("Negative Values =",tns)