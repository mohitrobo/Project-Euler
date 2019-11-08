#what is the 10001st prime number

from math import sqrt
import time
start = time.time()

#variable for prime number
prime = 3

#variable to count the number of primes
count = 1

#condition for while loop
check = True

while check:
    for i in range(2,int(sqrt(prime))+1):
        if (prime%i) == 0:
            break
    else:
        count += 1
        if count == 10001:
            check = False
            print("The 10001th prime number: {}".format(prime))
            
    prime +=2
end = time.time()
print(end-start)

