import time

start = time.process_time()

def reverse(newstring):
    if newstring == '':
        return ''
    print(newstring)
    return newstring[-1] + reverse(newstring[:-1])
        

s = "HelloThere!"
exp_s = "!erehTolleH"
rev_s = reverse(s)
if rev_s == exp_s :
    print(rev_s)
else:
    print(rev_s)
print(time.process_time() - start)