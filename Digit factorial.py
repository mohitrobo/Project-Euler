#Digit factorials
#In order to calculate factorial,there is a program. I will use math.factorial


from math import factorial as fact
import time

start = time.time()


#factorial of number from 0-9
f = [fact(0),fact(1),fact(2),fact(3),fact(4),fact(5),fact(6),fact(7),fact(8),fact(9)]

#store sum of numbers
summation = 0

#sum of factorials
def factorial_digit(n):
    sum_factorial = 0 #for storing the sum of factorial of digits
    while n:
        sum_factorial += f[n%10]
        n //=10
    return sum_factorial


for i in range(10,1854721):
    #check if sum is equal to number itself
    if factorial_digit(i) == i:
        summation += i



print(summation)
end = time.time()
print(end-start)
    
