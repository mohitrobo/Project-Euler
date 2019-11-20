#consecutive quadratic primes
from math import sqrt
import time
start = time.time()

#function for finding consecutive quadratic primes
def quad(a,b):
    count = 0 #for counting the prime values
    check = True #running a loop until consecutive prime numbers are there

    n = 0
    while check:
        z = n**2 + a*n + b

        #check for prime number
        if z>1:
            for p in range(2,int(sqrt(z))+1):
                if z%p == 0:
                    check = False
                    return count
            else:
                count += 1
            
        n = n+1

coeff,length = 0,0

#loop for coefficient values
for i in range(-999,1000):
    for j in range(-1000,1001):
        x = quad(i,j)
        if x > length:
            length = x
            coeff = i*j

end = time.time()
print("Length of primes: {}".format(length))
print("The product of coefficient is : {}".format(coeff))
print(end-start)
