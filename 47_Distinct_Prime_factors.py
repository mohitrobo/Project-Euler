import time

#create a function to find the prime factors
def primeFactors(n):
    #set to store prime factors
    prime_set=set()
    c = 2
    while(n > 1):
 
        if(n % c == 0):
            #print(c, end=" ")
            prime_set.add(c)
            n = n / c
        else:
            c = c + 1
    
    #return the length of the set containing prime factors
    return len(prime_set)
  

start=time.time()
#The value of i was chosen at random
#This is yet to be checked, as it should have been 2*3*5*7
i=132000
flag =True

#loop
while flag:
    if primeFactors(i)==4:
        i+=1
        if primeFactors(i)==4:
            i+=1
            if primeFactors(i)==4:
                i+=1
                if primeFactors(i)==4:
                    print(i-3)
                    flag =False
                    
    i+=1
    
end=time.time()
print("Time taken: ",end-start)
