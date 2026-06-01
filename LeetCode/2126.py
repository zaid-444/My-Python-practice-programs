# 2126. Destroying Asteroids

def asteroidsDes(mass,asteroids):
    asteroids.sort()
    res = False
    for st in asteroids:
        if st <= mass:
            mass += st
            res = True
        else:
            return False
    return res



mass = int(input("Enter mass value: "))
asteroids = [ int(n) for n in input("Enter asteroids: ").split() ]
print("~"*20)
print("Output:",asteroidsDes(mass,asteroids))
print("~"*20)