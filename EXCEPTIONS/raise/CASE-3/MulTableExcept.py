# Write a python program which will generate multiplication table for a given number.   1. if the given number is -VE then Hit NegNumError      2. if the given number is ZERO Generate ZeroError       3. if the given number is alpha-numeric then generate ValueError    4. If the number is +VE then Display Mul Table

class NegNumError(Exception):
    pass

class ZeroError(Exception):
    pass