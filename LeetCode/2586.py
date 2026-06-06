# 2586. Count the Number of Vowel String in Range

def vowelStrings(words,left,right):
    c = 0
    vowel = "aeiou"
    for i in range(left,right+1):
        if words[i][0] in vowel and words[i][-1] in vowel:
            c += 1
    return c


words = [ word for word in input("Enter Words: ").split() ]
left = int(input("Enter left value: "))
right = int(input("Enter right value: "))
res = vowelStrings(words,left,right)
print("~"*20)
print("Output:",res)
print("~"*20)