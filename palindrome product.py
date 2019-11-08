#Largest palindrome made from the product of two 3 digit numbers

import time
start = time.time()
#variable for palindrome product
palin_num = 0

#multiplication of two 3 digit values in variable a and b
for a in xrange(100,1000):
    for b in xrange(100,1000):
        num = str(a*b)  #convert multiplication into string so as to access the index value for comparison among index
        if (num==num[::-1]):
            palin_num = max(palin_num,int(num))

end = time.time()
print(palin_num)
print(end-start)

        
