import time
import re

start = time.process_time()

def fun(a,b):
    da = {}
    db = {}
    a = re.sub('\W+','',a).lower()
    b = re.sub('\W+','',b).lower()
    if len(a) != len(b):
        return False
    print(a,b)
    for i in a:
        try:
            da[i]
        except KeyError:
            da[i] = 1
        else:
            da[i] += 1
    for i in b:
        try:
            db[i]
        except KeyError:
            db[i] = 1
        else:
            db[i] += 1
    print(da,db)
    if da == db:
        return True
    else:
        return False

l1 = ['rail safety', 'RAIL! SAFETY!', 'Hi There']
l2 = ['fairy tales', 'fairy tales', 'Bye There']
for i in range(len(l1)):
    print(l1[i],l2[i],fun(l1[i],l2[i]))
print(time.process_time() - start)