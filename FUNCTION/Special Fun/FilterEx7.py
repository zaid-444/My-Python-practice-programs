# Write a python program which will implement the following
#          value = P2y$1h4#*o$n"
# obtain the alphabates
# obtain the speacial symbols
# obtain the digits

value = "P2y$1h4#*o$n"

alph = list(filter(lambda ch: ch.isalpha(),value))
dig = list(filter(lambda ch: ch.isdigit(), value))
sym = list(filter(lambda ch: not ch.isalnum(),value))

print("-"*50)
print("Word =",value)
print("-"*50)
print("Alphabates =",''.join(alph))
print("Digits     =",''.join(dig))
print("Symbols    =",''.join(sym))
print("-"*50)
