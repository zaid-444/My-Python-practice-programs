# 2114. Maximum Number of Words Found in Sentences

def mostWordsFound(sentences):
    count = 0
    for sen in sentences:
        senl = sen.split()
        wc = 0
        for i in senl:
            wc += 1
        if count <= wc:
            count = wc
    print("Biggest sentence word count =",count)

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

mostWordsFound(sentences)