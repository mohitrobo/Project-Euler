#Pandigital products

#taking range of a = 1 to 200 and b = 1 to 200
#multiply a and b
#store product in p
#make them as string and concatenate
#convert them in set and find the length
# 0 not allowed to be counted

import time

start = time.time()

#empty string to store a,b and p as a list
store = []

for a in xrange(1,200):
    for b in range(1,200):
        p = a*b

        #string conversion and concatenate and convert into set
        s = set(str(a)+str(b)+str(p))

        #check if 0 is present in set
        if '0' in s:
            pass
        else:
            if len(s) == 9:
                store.append([a,b,p])
            else:
                pass


print(store)
