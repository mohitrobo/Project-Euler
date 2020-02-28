#Double-base palindromes check for first 1 million numbers
#use slicing to check palindrome

import time

start = time.time() 
           
#store palindrome values
#palin_list = []

#sum to store the sum of palindrome numbers
sum_palin = 0

for num in xrange(1,1000000):
    x = str(num) #convert it into string

    if x == x[::-1]: #check for reverse of number
        deci_bin = bin(num)
        if deci_bin[2:] == deci_bin[2:][::-1]:
            sum_palin += num



end = time.time()        
#print(palin_list)
print(sum_palin)
print(end - start)
