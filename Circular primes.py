#Circular primes for upto 1000 numbers
#use slicing to circularly rotate the number 



#list to store the circular prime
list_prime = []


for num in xrange(10,1000):
    x = str(num)
    prime_number = []
    for i in xrange(0,len(x)):
        y = int(x[i:len(x)] + x[0:i])
        for j in range(2,y):
            if (y%j) == 0:
                break
        else:
            prime_number.append(y)
            continue
        break

    if len(prime_number) == len(x):
        list_prime.extend(prime_number)
        
        
            

#for slicing to circularly rotate number
#for i in range(0,len(x)):
 #   y.append(x[i:len(x)] + x[0:i])

print(set(list_prime))
