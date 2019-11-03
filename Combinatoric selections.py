#Combinatoric selections
#In the question it is already given that the first value that exceeds 1 million is for n=23 and r=10

#1. use the combination formula


import time
from math import factorial as f

start = time.time()

n = 23
count = 0

while(n<101):
    for r in xrange(0,n+1):
        value = f(n)/(f(r)*f(n-r))
        if value > 1000000:
            count += 1

    n += 1
        

print(count)

end = time.time()
print(end - start)

    
