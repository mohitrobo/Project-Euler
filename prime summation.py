#summation of prime numbers

import time
import math

#function to find prime numbers
def prime(num):
    #prime_store = []
    sum_prime = 0
    lower = 2
    for x in xrange(lower, num+1):
        for i in xrange(2,int(math.sqrt(x))+1):
            if (x%i) == 0:
                break
        else:
            #prime_store.append(x)
            sum_prime += x

    #return the list
    return sum_prime

#ask for maximum value upto which prime number is to be found
prime_input = int(input("Enter the maximum value upto which prime number is to be found: "))
prime_summation = prime(prime_input)
#print(prime_list)
print("The summation of prime numbers: {}".format(prime_summation))


