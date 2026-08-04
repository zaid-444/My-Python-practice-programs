# 3014. Minimum Number of Pushes to Type Word |

def minimumPushes(word):
    d = {}
    for ch in word:
        d[ch] = d.get(ch,0) + 1
    lst = list(d.values())
    lst.sort(reverse=True)
    ans = 0
    for i in range(len(lst)):
        ans += lst[i]*(i//8+1)
    return ans