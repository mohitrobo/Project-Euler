#prime number generation

import time

start = time.time()

lower = 3
upper = 50

prime = [2]

for num in xrange(lower,upper+1,2):
    for i in xrange(2,num):
        if (num%i) == 0:
            break
    else:
        print(num)
    
end  = time.time()
print(end - start)
