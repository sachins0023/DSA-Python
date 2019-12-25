# import time

# start = time.process_time()

# def fun():
#     pass

# l = []
# for i in l:
#     print(fun(i))
# print(time.process_time() - start)

import time

start = time.process_time()

def rev(num):
    def reverse(num):
        if num<10:
            return num
        return (10**(len(str(num))-1))*(num%10)+reverse(num//10)
    if num:
        return int(reverse(abs(num))*num/abs(num))
    else:
        return 0 

l = [9284, 78, -91192, 0, -19, -4,4, 19, 500]
for i in l:
    print(i, rev(i), sep=':')
print(time.process_time() - start)
