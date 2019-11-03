#Champernowne's constant

import time

start = time.time()

#list to store the values
#champer = []

#empty string to store the numbers
a = ''

for i in xrange(1,1000000):
    a += str(i)
    if len(a) >= 1000000:
        break
    
####################################
    #OR by storing in list which takes a lot of time
####################################
    
    #if len(str(i)) == 1:
        #champer.append(i)
    #else:  #length of i >= 2
        #s = str(i)
        #for j in xrange(0,len(s)):
            #champer.append(int(s[j]))
        #if len(champer) >= 1000000:
            #break


#the 1st element of champer list has index 0
#10th element index = 9
#100th element index = 99

end = time.time()

#print(champer[0]*champer[9]*champer[99]*champer[999]*champer[9999]*champer[99999]*champer[999999])

d1 = int(a[0])
d10 = int(a[9])
d100 = int(a[99])
d1000 = int(a[999])
d10000 = int(a[9999])
d100000 = int(a[99999])
d1000000 = int(a[999999])
print(d1*d10*d100*d1000*d10000*d100000*d1000000)
print(end - start)
