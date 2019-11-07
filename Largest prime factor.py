#program to find the largest prime factor of a number

import time
start = time.time()
#Enter the number for which prime factor needs to be found
num = 600851475143

#variable for storing prime factors
prime_factor = 0

x = 2

#for finding and incrementing the prime factors
while x>1:
     for i in xrange(2,x): #for finding prime numbers
        if (x%i) == 0:
            x+=2
            break
    #Once prime factor is found
    else:
        #while loop to check if the same prime factor can do the division
        while(num%x == 0): 
            num = num/x
        prime_factor = max(prime_factor,x)
        if(x%2==0):
            x+=1
        else:
            x+=2

    #Once the quotient obtained is 1
    if num == 1:
        break

print(prime_factor)
end = time.time()
print(end-start)
