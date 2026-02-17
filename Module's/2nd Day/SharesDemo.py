import Shares,time,importlib

def dispshares(d):
    print("-"*40)
    print("ShareName\tShareValue")
    print("-"*40)
    for sn,sv in d.items():
        print("{}\t\t{}".format(sn,sv))
    print("-"*40)
    
d = Shares.shareinfo()
dispshares(d)

print("Going to sleep for 10 Secs")
time.sleep(10)
print('='*40)
print("Coming out-off sleep after 10 Secs")
importlib.reload(Shares) # importlib(deprecated from imp module)

d = Shares.shareinfo()
dispshares(d)