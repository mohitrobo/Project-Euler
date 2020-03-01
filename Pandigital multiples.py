#Pandigital multiples
#the maximum value upto which the multiplication can be done is 9999

import time

start = time.time()

max_number = 1

for num in xrange(1,10000):
    #string variable to store concatenated number
    s = ""
    
    #multiply with 1 to 9
    for i in xrange(1,10):
        s += str(num * i)

        #check if length obtained is 9
        if len(s) == 9:
            #convert into set to check if there is no repetition
            a = set(s)
            if len(a) == 9:
                #check for the presence of 0
                if '0' in a:
                    break
                else:  #0 not present
                    max_number = max(max_number,int(s))


end = time.time()

print(max_number)
print(end - start)
