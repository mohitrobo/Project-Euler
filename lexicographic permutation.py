#there is still a confusion to find permutation
#itertools is used 



#from math import factorial
#def perm(n, s):
 #  if len(s)==1: return s
  # q, r = divmod(n, factorial(len(s)-1))
   #return s[q] + perm(r, s[:q] + s[q+1:])

#L = 19
#print "Project Euler 24 Solution = ", perm(L-1, '4321')




#another set of program
from itertools import permutations
x = list(permutations("1234"))
print(x)
