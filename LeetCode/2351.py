# 2351. First Letter to Appear Twince

def repeatChar(s):
    st = set()
    for ch in s:
        if ch not in st:
            st.add(ch)
        else:
            return ch
    

s = input("Enter a String: ")
print("-"*30)
print(f"({repeatChar(s)}) Appear Twice")
print("-"*30)