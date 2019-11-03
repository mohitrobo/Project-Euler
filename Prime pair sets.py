#Prime pair sets
#Go to this site for more information
#https://blog.dreamshire.com/project-euler-60-solution/

#1.) create a list of prime number upto 10000, except 2 becoz concatenating 2 will always be divisible
#2.) Find pairs of concatenable primes and then use each set to find intersections with other sets.
#So, for 3 the other primes less than 1,000 that are concatenable are:
#3 [7, 11, 17, 31, 37, 59, 67, 73, 109, 137, 191, 229, 271, 331, 359, 373, 449, 467, 499, 541, 557, 607, 613, 617, 673, 701, 719, 733, 739, 823, 929, 947]
#So, we need to search each of these sets starting with 7:
#7 [19, 61, 97, 109, 127, 229, 283, 433, 487, 523, 541, 547, 673, 691, 757, 823, 829, 853, 883, 937]
#The intersection of these sets is:
#{109, 229, 541, 673, 823}
#Check the above set for 2 primes that can concatenate to make other primes and a 4 prime set is found {3, 7, 109, 673}

import time
import pdb
import math


start = time.time()

#function to check if prime
def is_prime(num):
    for i in xrange(2,int(math.sqrt(num))+1): #concatenated number will never become even
        if (num%i) == 0:
            return False
    else:
        return True



#function to check if concatenation of number is prime
def concat(x,ylist):
    count = []
    for m in xrange(0,len(ylist)):
        if is_prime(int(str(x)+str(ylist[m]))) and is_prime(int(str(ylist[m])+str(x))):
           count.append(ylist[m])
    return count
           
            



#list to store prime
#the prime number is stored from number 3 as if 2 is concatenated with any number it will be divisible
prime = []
for num in xrange(3,10000,2):
    for i in xrange(3,num):
        if (num%i) == 0:
            break
    else:
        prime.append(num)

#print(len(prime))

#list to store primes which are concatenable
#concatlist = []

#pop the first prime from list
flag = True
e = 0 #index to be poped from the list of prime
while e >= 0:
    #pdb.set_trace()
    new_prime = prime[:] #copying a list to another list
    concatlist = [] #list that will finally store the 5 prime numbers
    x = new_prime.pop(e)
    for i in xrange(0,4):
        new_prime = concat(x,new_prime)
        concatlist.append(x)
        if len(new_prime) == 0:
            break
        elif len(new_prime) == 1 and i == 3:
            flag = False
            concatlist.append(new_prime.pop(0))
            break
        x = new_prime.pop(0)
    e += 1
    if flag == False:
        break
        

print(concatlist)

end = time.time()
print(end - start)


                            
                        
        
        
