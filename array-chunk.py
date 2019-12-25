import time

start = time.process_time()

def fun(arr, size):
    if len(arr)<size:
        return arr
    if len(arr[size:]):
        return arr[:size],fun(arr[size:],size)
    else:
        return arr[:size]

l = [[1,2,3,4,5,6,7,8],[1,2],[1,2,3,4,5],[1,2,3,4],[1,2,3,4,5,6]]
k = 3
for i in l:
    print(fun(i,k))
print(time.process_time() - start)