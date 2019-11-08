#summation of prime numbers

import time
import math

start = time.time()

#function to find prime numbers
def prime(num):
    sum_prime = 2
    lower = 3
    for x in xrange(lower, num+1,2):
        for i in xrange(2,int(math.sqrt(x))+1):
            if (x%i) == 0:
                break
        else:
            sum_prime += x

    #return the sum
    return sum_prime

prime_summation = prime(2000000)
end = time.time()
print("The summation of prime numbers: {}".format(prime_summation))
