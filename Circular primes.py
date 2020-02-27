#Circular prime below 1 million
#use slicing to circularly rotate the number 

import time
import math

start = time.time()

#list to store the circular prime
list_prime = []

#below 100 there are 13 such primes as given in the question
#list to store circular prime
for num in xrange(100,1000000):
    x = str(num)
    prime_number = []
    for i in xrange(0,len(x)):
        y = int(x[i:len(x)] + x[0:i])
        #This will loop from 2 to int(sqrt(x))
        for j in xrange(2,int(math.sqrt(y))+1):
            if (y%j) == 0:
                break
        else:
            prime_number.append(y)
            continue
        break

    if len(prime_number) == len(x):
        list_prime.extend(prime_number)


count = len(set(list_prime)) + 13
print(count)

end = time.time()
print(end-start)
