#Powerful digit sum

import time

start = time.time()

#1. natural numbers are >= 1
#2. 1<a<100, 1<b<100
#3. calculate a^b, convert into string
#4. add each digit
#5. compare for highest sum




#######################################
#One line code
#######################################

print max(sum(map(int, str(a**b))) for a in xrange(100) for b in xrange(100))


##########################################
#This is another way
##########################################


#maximum = 0

#for a in xrange(1,100):
    #for b in xrange(1,100):
        #add = 0
        #x = pow(a,b)
        #while x != 0:
            #add += x%10
            #x //= 10
        #maximum = max(add,maximum)

#print(maximum)

end = time.time()
print(end - start)
