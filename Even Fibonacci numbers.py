#Even Fibonacci numbers

import time

start = time.time()

#initial two numbers of the sequence
a,b = 1,2

#variable to store addition
add = 2

while True:
    if (a+b) > 4000000: #upto value = 4 million
        break
    if (a+b)%2 == 0:
        add += (a+b)

    a,b = b,a+b

print("the total sum of even numbers: {}".format(add))

end = time.time()
print(end - start)
