# 58. Length of Last Word

def lenOfLastWord(s):
    lst = s.split()
    return len(lst[-1])
