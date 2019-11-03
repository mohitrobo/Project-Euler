#Lattice path

import math

#function to calculate lattice path for a square matrix
def lattice(n): #nxn matrix
    n_fact = math.factorial(n)
    return math.factorial(2*n) / (n_fact * n_fact)


path = int(input("Enter the size of square matrix(n x n),provide only n: "))
print(lattice(path))

