#Difference of the sum of square and square of sum of first 100 numbers

import time
start = time.time()
#variable to store sum of square
sum_square = 0
#variable to store sum of numbers
sum_num = 0

for x in range(1,101):
    sum_square += x**2
    sum_num += x

end = time.time()
print("sum of square: {}".format(sum_square))
print("square of sum of number: {}".format(sum_num**2))
print("Difference of the square of sum and sum of square: {}".format(sum_num**2 - sum_square))
print(end-start)
