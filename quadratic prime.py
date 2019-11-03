#consecutive quadratic primes
#for coefficient a,b ranging from -100 to 100

#function for finding consecutive quadratic primes
def quad(a,b):
    y = [] #for storing the prime values
    check = True #running a loop until consecutive prime numbers are there

    n = 0
    while check:
        z = n**2 + a*n + b

        #check for prime number
        if z>1:
            for p in range(2,z):
                if z%p == 0:
                    check = False
                    return (a,b,len(y))
            else:
                y.append(z)
            
        n = n+1


long_prime = [0,0,0]

#loop for coefficient values
for i in range(-999,1000):
    for j in range(-1000,1001):
        x = quad(i,j)
        if x[2] > long_prime[2]:
            long_prime = x


print("Length of primes: {}".format(long_prime[2]))
print("coefficient (a,b) with maximum length of quadratic primes are: ({},{})".format(long_prime[0],long_prime[1]))
print("The product of coefficient is : {}".format(long_prime[0]*long_prime[1]))
