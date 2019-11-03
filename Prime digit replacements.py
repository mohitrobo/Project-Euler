#Prime digit replacements

import time
from collections import Counter

start = time.time()

#Generate prime numbers from 100 to 60000
prime = []
for num in xrange(100,60000):
    for i in xrange(2,num):
        if (num%i) == 0:
            break
    else:
        prime.append(num)

#print(len(prime))




#save only those prime numbers which has repeatition of digits >= 2
new_prime = []
for i in prime:
    s = str(i)
    if (len(s) - len(set(s))) >= 1:
        new_prime.append(i)

#print(len(new_prime))




#1.Pick each prime number
#2.replace the repetition number by 0-9 and save it in a list named "replaced"
#3.check if the new list is present in the new prime number list
#4.count the occurance and if it is = 7 break the loop        
n = 0
flag = True
while flag:
    s = str(new_prime[n])
    counter = Counter(s)
    #from values obtain keys that are to be replaced
    for k,v in counter.items():
        replaced = []
        occur = 0
        if v >= 2:
            for i in xrange(0,10):
                replaced.append(int(s.replace(k,str(i))))
            for j in replaced:
                if j in new_prime:
                    occur += 1
            if occur == 7:
                x = [] #store only prime number out of 10 numbers obtained
                for r in replaced:
                    if r in new_prime:
                        x.append(r)
                print(x)
                flag = False
                break
    n += 1




#check if the new list is present in the new prime number list
#count the occurance and if it is = 7 break the loop








end = time.time()
print(end - start)
