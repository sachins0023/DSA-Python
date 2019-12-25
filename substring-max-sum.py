import time
from copy import copy

start = time.process_time()

#using sliding window
def fun(arr, k):
    if len(arr)<=k:
        return arr, sum(arr)
    sub_arr = arr[:k]
    maxsum = sum(sub_arr)
    maxsumarr = copy(sub_arr)
    for i in arr[k:]:
        sub_arr.pop(0)
        sub_arr.append(i)
        if sum(sub_arr)>maxsum:
            maxsum = sum(sub_arr)
            maxsumarr = copy(sub_arr)
    return maxsumarr, maxsum

l = [[2,7,3,6,5,0,7,8],[8,2,3,5,4,3],[1,2,3,9,8,7,6,5,4]]
k = 3
for i in l:
    print(i, fun(i,k))
print(time.process_time() - start)