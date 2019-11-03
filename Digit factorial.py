#Digit factorials
#In order to calculate factorial,there is a program. I will use math.factorial
#will check factorial upto 999


import math
import time

start = time.time()

#list to store the number
digit_factorial = []

for i in range(10,1000000):
    sum_factorial = 0 #for storing the sum of factorial of digits
    #convert integer to string
    s = str(i)
    for j in s:
        sum_factorial += math.factorial(int(j))

    #check if sum is equal to number itself
    if i == sum_factorial:
        digit_factorial.append(i)


#sum to store the summation of numbers
sum_store = 0
print(digit_factorial)
for j in xrange(0,len(digit_factorial)):
    sum_store += digit_factorial[j]

print(sum_store)
    
