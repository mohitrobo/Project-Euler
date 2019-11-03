#Pentagon numbers

import math

#function to check pentagon numbers(wikipedia)
def pentagon(num):
    x = (math.sqrt(24*num+1) + 1)/6
    if x>0: #if x is positive
        y = math.modf(x)
        if y[0] == 0:
            return True
        else:
            return False
    else:
        return False


check = True
#list to store pentagon numbers
P = []
n = 1

while check:
    P.append(n * (3*n-1)/2)
    for j in xrange((len(P)-2),-1,-1):
        a = P[len(P)-1]
        b = P[j]
        if pentagon(a+b) and pentagon(a-b):
            print(a-b)
            check = False
            break
    n += 1





    
