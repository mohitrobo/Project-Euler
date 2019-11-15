#to find the prime factors of a number
#Amicable numbers

import time
start = time.time()

def prime_factor(x):
    amicable_sum = 0
    for i in range(1,(x/2)+1):
        if x%i == 0:
            amicable_sum += i

    return amicable_sum

#list to store amicable numbers
amicable_list = []


#search amicable numbers within 1000
for i in range(1,10000):
    x_sum = prime_factor(i)
    y_sum = prime_factor(x_sum)
    if i == y_sum:
        if x_sum != y_sum:
            amicable_list.append(i)
            
end = time.time()
print("The sum of the unique amicable numbers: {}".format(unique_sum))
print(end-start)
