#Pandigital prime

#the digits 1st from 1-9
#then 1-8 if not found in 9 digit, then reduce it further

#variable to store max prime
prime = 1

###################################
#This is one way fo doing it
###################################

#for num in xrange(2,10000):
 #   for i in xrange(2,num):
  #      if (num%i) == 0:
   #         break
    #else:
     #   if len(str(num)) == len(set(str(num))):
      #      prime = max(prime,num)

#print(prime)


####################################
#Another way of doing it
####################################


from itertools import permutations

a = '123456789'
x = len(a)
check = True

while check:
    p = list(permutations(a[:x]))

    for i in p[::-1]:  #starting from maximum number
        num = int(''.join(i))
        #check if prime number
        for j in xrange(2,num):
            if (num%j) == 0:
                break
        else:
            prime = max(prime,num)
            check = False
            break
            

    x -= 1


print(prime)
