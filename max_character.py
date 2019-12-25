import time

start = time.process_time()

def fun(newstring):
    d = {}
    maxvalue = None
    for i in newstring:
        try:
            d[i]
        except KeyError:
            d[i] = 1
            if maxvalue is None:
                maxvalue = i
        else:
            d[i] += 1
            if d[maxvalue]<d[i]:
                maxvalue = i
    return maxvalue, d[maxvalue]            

l = ['gagaaaagagagaa', 'oolallaoolalaa', 'malayalam']
for i in l:
    print(fun(i))
print(time.process_time() - start)