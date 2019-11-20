#Lexicographic permutation
#itertools is used 

import time
from itertools import permutations
start = time.time()

x = list(permutations("0123456789"))
print(''.join(x[999999]))
end = time.time()
print(end-start)
