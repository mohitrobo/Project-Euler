#Coin sums
#solving using mathematical equation

import time
start = time.time()

counter = 0
for a in xrange(0,3):  #for 100p denomination
    for b in xrange(0,1+(200-100*a)/50):  #for 50p denomination
        for c in xrange(0,1+(200-100*a-50*b)/20):  #for 20p denomination
            for d in xrange(0,1+(200-100*a-50*b-20*c)/10):  #for 10p denomination
                for e in xrange(0,1+(200-100*a-50*b-20*c-10*d)/5):  #for 5p denomination
                    for f in xrange(0,1+(200-100*a-50*b-20*c-10*d-5*e)/2):  #for 2p denomination
                        counter += 1



counter += 1 #for 1 200p denomination
end = time.time()
print("The number of ways are: {}".format(counter))
print("The total duration for solving the problem: {}".format(end-start))
