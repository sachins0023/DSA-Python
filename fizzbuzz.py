import time

start = time.process_time()

def fun(num):
    if num<=1:
        return num
    if num%15==0:
        return fun(num-1), "fizzbuzz"
    if num%5==0:
        return fun(num-1), "buzz"
    if num%3==0:
        return fun(num-1), "fizz"
    else:
        return fun(num-1), num
            

l = [27,4,0,15,19]
for i in l:
    print(fun(i))
print(time.process_time() - start)