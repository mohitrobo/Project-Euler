#Digit Cacelling Fractions

#two digit numerator and denominator to find non-trivial solutions
#non-trivial solutions should not include 0 in both of them like, 10/20,20/30,etc
#ratio has to be < 1 i.e N<D


import time

start = time.time()

#list to store the fractions
non_fractions = []

for N in xrange(10,100):
    for D in xrange(11,100):
        common = []  #for storing common digits
        if N<D :  #fraction < 1
            if (N%10 == 0) and (D%10 == 0):  #this gives trivial solution
                pass
            else:  #non-trivial solution
                x = str(N)
                y = str(D)
                if (x[0] in y) or (x[1] in y):  #common term between values
                    for i in set(x):
                        for j in set(y):
                            if i==j:
                                common.append(i)
                    for k in range(0,len(common)):
                        if x.count(common[k])==2 and not y.count(common[k])==2:
                            n = int(x[0])
                            d = int(y.replace(common[k],''))
                            if d != 0:
                                if round(float(N)/float(D),7) == round(float(n)/float(d),7):
                                    non_fractions.append([N,D,n,d])
                        elif not x.count(common[k])==2 and y.count(common[k])==2:
                            n = int(x.replace(common[k],''))
                            d = int(y[0])
                            if d != 0:
                                if round(float(N)/float(D),7) == round(float(n)/float(d),7):
                                    non_fractions.append([N,D,n,d])
                        else:        
                            n = int(x.replace(common[k],''))
                            d = int(y.replace(common[k],''))
                            if d != 0:
                                if round(float(N)/float(D),7) == round(float(n)/float(d),7):
                                    non_fractions.append([N,D,n,d])
                        

                else:
                    pass


        else:
            pass


end = time.time()
print(non_fractions)
print(end-start)

