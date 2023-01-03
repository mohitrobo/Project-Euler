#1.) Permute the digits 0-9
#2.) Store in the list
#3.) Join each element of the list
#4.) Iterate through the list and verify the required condition

import time
#permutation method
from itertools import permutations

start=time.time()
#The numbers to be permuted
a='0123456789'

#Store the permuted numbers in a list
p = list(permutations(a))

add_numbers=0
#Iterate through the permutations
for i in p:
    s=''.join(i)
    
    #conditions to be met
    if (int(s[1:4])%2==0 and int(s[2:5])%3==0 and int(s[3:6])%5==0 and int(s[4:7])%7==0 
        and int(s[5:8])%11==0 and int(s[6:9])%13==0 and int(s[7:10])%17==0):
            add_numbers+=int(s)
            
            
print(add_numbers)

end=time.time()
print('Time taken: ',end-start)
