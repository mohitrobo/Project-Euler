#Goldbach's other conjecture

import math
import time

start = time.time()


#function to generate prime number
def is_prime(z):  #upto the value of composite number
    for a in xrange(2,z):
        if (z%a) == 0:
            return False
            break
    else:
        return True



#0. Append the prime numbers
#1. If not prime than it has to be odd composite number
#1. loop to first find composite number(odd) that is not Goldbach
#2. as soon as the value which is not Goldbach, end the loop


flag = True

num = 3

prime = [2]

while flag:
    if is_prime(num):
        prime.append(num)
    else:
        for i in prime:
            if math.sqrt((num-i)/2) == int(math.sqrt((num-i)/2)):  #if Goldbach
                break
        else:
            print num
            flag = False

    num += 2
                                           


end = time.time()
print(end-start)
            





                    
