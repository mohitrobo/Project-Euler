#Spiral primes


import time

start = time.time()


#function to check prime
def prime(num):
    for i in xrange(3,num,2):
        if (num%i) == 0:
            return False
    else:
        return True

#list to store spiral diagonals
spiral = [1] #the center value is stored first

flag = True

#start from even value
n=2

j=1 #used in even condition
k=1 #used in odd condition
count = 0 #count the number of primes

while flag:
    if n%2 == 0:  #even number
        a = pow(n,n) + 1
        if prime(a):
            count += 1
        b = pow(n,n) + (2*j+1)
        if prime(b):
            count += 1
        spiral.extend([a,b])
        j += 1

    else:  #odd number
        a = pow(n,n)
        b = a - (6*k)
        if prime(b):
            count += 1
        spiral.extend([a,b])
        k += 1
        #check for the percentage
        if ((float(count)/float(len(spiral)))*100) < 10.0:
            flag = False
            print(n)

    n += 1


end = time.time()
print(end - start)







        








        
