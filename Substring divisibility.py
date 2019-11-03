#Sub-string divisibility
#first permutation of 10 digits is found
#three digit divisibility is checked with prime numbers(2-987)

from itertools import permutations

#variable to store addition of sub-string
substring = 0

s = '0123456789'  #d1 to d10

perm = list(permutations(s))

for p in perm:
    x = str(''.join(p))
    if (int(x[7:10]))%17 == 0:
        if (int(x[6:9]))%13 == 0:
            if (int(x[5:8]))%11 == 0:
                if (int(x[4:7]))%7 == 0:
                    if (int(x[3:6]))%5 == 0:
                        if (int(x[2:5]))%3 == 0:
                            if (int(x[1:4]))%2 == 0:
                                substring += int(x)


print(substring)
            
        
        
