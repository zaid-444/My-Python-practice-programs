from NameExcept import NameValidError,ZeroLenError

def namevalidpro(name):
    if len(name) == 0:
        raise ZeroLenError
    else:
        valid = True
        words = name.split()
        for word in words:
            if not word.isalpha():
                valid = False
                break
        if valid:
            return "({}) Is Valid Name".format(name)
        else:
            raise NameValidError


namevalidpro("Zaid Shaikh")