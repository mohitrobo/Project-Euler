#Triangular, pentagonal and hexagonal number
#question has already told us to find the next triangle number
#after T[284] = 40755
#therefore for n>285

import time
import math

start = time.time()

#function to check pentagonal
def is_pentagonal(p):
    if (1+math.sqrt(24*p+1))%6 == 0:
        return True
    return False


#function to check hexagonal
def is_hexagonal(h):
    if (1+math.sqrt(8*h+1))%4 == 0:
        return True
    return False


n = 286 #n>285


#list for triangular
T = []


while True:
    triangle = (n*(n+1))/2 #triangle number
    T.append(triangle)
    if is_pentagonal(triangle) and is_hexagonal(triangle):
        print(triangle)
        print(len(T))
        break
    n += 1
        
end = time.time()
print(end - start)
