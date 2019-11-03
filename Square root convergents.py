#Square root convergents

import time

start = time.time()


#1. the iterations start from 1-1000 including 1000th iteration
#2. https://math.stackexchange.com/questions/730349/convergents-of-square-root-of-2


p = 1
q = 1


count = 0
#iterations from 1 to 1000
for i in xrange(1,1001):
    a1 = p+2*q  #numerator
    b1 = p+q  #denominator
    if len(str(a1)) > len(str(b1)):
        count += 1

    p = a1
    q = b1
    
print(count)

    

end = time.time()
print(end - start)
    






