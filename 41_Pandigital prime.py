#1.) Find the highest possible prime number.
#2.) Every digit from 1-->n should only appear once.
#3.) The highest value of n=9.
#4.) Checking for the prime number can only start from the highest possible value 987654321.
#5.) Since the digit has to only appear once, no need to iterate from highest to lowest.
#6.) Use the concept of permutation.
#7.) In permutation, the values are stored in a list.
#8.) As you perform permutation for digits 1-->9, reverse the list as highest value needs to be checked first.
#9.) If prime number is not found for digits 1-->9, decrement and check for digits 1-->8 and perform the same operations.

import time
from math import*
#permutation method
from itertools import permutations


#check for prime number
def isprime(n):
    #check if n is divisible by 3
    if n%3==0:
        return False
    
    #check from 5 to square root of n
    #Iterate k by k+6(step)
    for k in range(5,floor(sqrt(n)),6):
        if (n % k == 0 or n % (k + 2) == 0):
            return False
        
    return True
  
  
  
# start the timer
start=time.time()

a='123456789'
j=9
flag=True

while flag:
    #permute the digits from 0-->j
    p = permutations(a[:j])
    #Reverse the list
    p = list(p)[::-1]

    for i in p:
        #Since each element of the list are tuple containing the digits as string, join them and convert to integer
        number=int(''.join(i))
        if number%2!=0:  #Check if not even
            if (number+1) % 6 == 0 or (number-1) % 6 == 0: #Basic condition for being a prime number
                if isprime(number): #Call the function to verify if prime number
                    print(number)
                    flag=False
                    break
                        
    j-=1

end=time.time()
print('time taken: ',end-start)

