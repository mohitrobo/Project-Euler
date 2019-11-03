#prime permutations

from itertools import permutations, combinations


#list to store prime number from 1000 to 10000
prime = []
for num in xrange(1000,10000):
    for i in xrange(2,num):
        if (num%i) == 0:
            break
    else:
        prime.append(num)

#print(len(prime))



#1. pick each prime number
#2. find permuatation of that prime number
#3. check if those permutation values are available in prime list >=3 and store in another list    
#4. select 3 values from the list and sort it and find difference and check if difference is equal



#list to store the 3 number that are prime permutations
per_prime = []

#check for every prime
for p in prime:

    #we don't want to check for prime number = 1487
    #we only want to find the other group
    if p == 1487:
        pass
    else:
        #convert into string and find permutations
        s = list(set(permutations(str(p))))
        c = []
        for q in s:
            c.append(int(''.join(q)))

        e = 0  #to check if number of values are >=3 
        #list to store sequence
        sequence = []
        for j in c:
            if j in prime:
                sequence.append(j)
                e += 1

        if e>=3:
            combine = list(combinations(sequence,3))
            for k in xrange(0,len(combine)):
                x = sorted(combine[k])
                if x[2]-x[1] == x[1]-x[0]:
                    per_prime.append(combine[k])
                    break
                    #print(per_prime)


print(set(per_prime))













        
            
