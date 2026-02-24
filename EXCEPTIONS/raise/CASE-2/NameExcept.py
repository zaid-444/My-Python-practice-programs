# Write a python program which will validate the name of Student
# Name must contain only a single word or multiple words separated by space only (only alphabates)
# Name should not contain digits
# Name should not contain speacial symbols

class NameValidError(BaseException):
    pass

class ZeroLenError(Exception):
    pass