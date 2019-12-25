# import time

# start = time.process_time()
# print(time.process_time() - start)


import time

start = time.process_time()
def palindrome(newstring):
    if newstring == '' or len(newstring)==1:
        return True
    if newstring[0].lower()==newstring[-1].lower():
        return palindrome(newstring[1:-1])
    else:
        return False

a = "Malayalam"
b = "english"
c = "a"
print(a, palindrome(a), b, palindrome(b), c, palindrome(c))


print(time.process_time() - start)