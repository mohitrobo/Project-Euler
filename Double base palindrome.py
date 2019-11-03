#Double-base palindromes check for first 1000 numbers
#use slicing to check palindrome

import time

start = time.time()

#function for checking palindrome
def palindrome(num):
    x = str(num) #convert it into string

    if x == x[::-1]: #check for reverse of number
        deci_bin = bin(num)
        if deci_bin[2:] == deci_bin[2:][::-1]:
            palin_list.append([num,deci_bin[2:]])

        

            
#store palindrome values
palin_list = []

for p in xrange(11,1000):
    palindrome(p)


end = time.time()        
print(palin_list)
print(end - start)



            
