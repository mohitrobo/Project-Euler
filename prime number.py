
import time
import math
#import pdb

start = time.time()

lower = 2
upper = 10000

#pdb.set_trace()
a = []
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            a.append(num)

print(len(a))
end = time.time()
print(end - start)


#################################################
#ANOTHER METHOD
#################################################

start1 = time.time()
b = []
for num in xrange(lower,upper+1):
    if num > 1:
        #This will loop from 2 to int(sqrt(x))
        for i in xrange(2,int(math.sqrt(num))+1):
            if (num%i) == 0:
                break
        else:
            b.append(num)
        
print(len(b))
end1 = time.time()
print(end1-start1)
            
        
