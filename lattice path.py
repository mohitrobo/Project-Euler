#Lattice path
import time
import math
start = time.time()

#function to calculate lattice path for a square matrix
def lattice(n): #nxn matrix
    n_fact = math.factorial(n)
    return math.factorial(2*n) / (n_fact * n_fact)


print(lattice(20))
end = time.time()
print(end-start)

