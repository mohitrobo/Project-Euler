#Truncatable primes


def prime(num):
    for i in xrange(2,num):
        if (num%i) == 0:
            return 0
            break
    else:
        return 1





#list to store prime numbers
list_prime = []


for number in xrange(11,1000):
    x = str(number)
    a = 1
    b = 1
    for j in xrange(0,len(x)):
        a *= prime(int(x[j:len(x)] + x[0:j]))
        if a == 0:
            break
    else:
        z = x[::-1]
        for k in xrange(0,len(z)):
            b *= prime(int(z[k:len(x)] + z[0:k]))
            if b == 0:
                break
        else:
            list_prime.append(number)

print(list_prime)
            
    
