#1.) odd + even = odd
#2.) odd(composite number)=odd(prime number) +2*(x)^2(even number)
#3.) Rearranging the equation, x=sqrt((odd(composite)-odd(prime))/2)----> x needs to be perfect square
#4.) value of x needs to be verified
#5.) Since odd number needs to be considered and 2 is the only even prime number, no need to consider 2 to check prime number
#6.) Start from value 3, iterate thorugh odd numbers to check if prime or composite.
#7.) If prime, store in list p and if composite, put in the formula to verify the perfect square(iterating through the prime number list)

import time
from math import sqrt

#check for prime number
def isprime(n):
    """function to check if the given
    number is prime or not"""
    if n % 2 == 0:
        return False
    else:
        for k in range(3, int(n**0.5+1),2):
            if n % k == 0:
                return False
        return True

      
start=time.time()
flag=True
prime=[]
#Iterate through the numbers starting from 3 and only odd numbers
i=3
while flag:
    if isprime(i):
        prime.append(i)
    else:
        for j in prime:
            s=sqrt((i-j)/2)
            if int(s)-s==0:
                break
        else:
            print(i)
            flag=False
    
    i+=2
    
end=time.time()
print("Time taken: ",end-start)
