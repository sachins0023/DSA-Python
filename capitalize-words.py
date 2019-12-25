import time

start = time.process_time()

def fun(newstring):
    newarr = newstring.split(' ')
    for i in range(len(newarr)):
        if newarr[i][0].isalpha():
            newarr[i] = newarr[i][0].upper()+newarr[i][1:]
        else:
            j=1
            while(j<len(newarr[i])):
                if not newarr[i][j].isalpha():
                    j+=1
                else:
                    newarr[i] = newarr[i][:j]+newarr[i][j].upper()+newarr[i][j+1:]
                    break
                    
    return " ".join(newarr)

l = ['hello there human', 'what a !wonderful day', 'i got 99 problems', 'you know nothing john snow !', '21guns']
for k in l:
    print(fun(k))
print(time.process_time() - start)