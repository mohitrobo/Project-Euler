#Even Fibonacci numbers

import time

start = time.time()

#initial two numbers of the sequence
a,b = 1,2

#initial value for addition
add = 2

while (a+b)<=4000000:
    if (a+b)%2 == 0:
        add += (a+b)

    a,b = b,a+b

print("the total sum of even numbers: {}".format(add))

end = time.time()
print(end - start)
