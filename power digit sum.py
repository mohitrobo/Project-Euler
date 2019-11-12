#sum of the digits obtained from 2^value

import math
import time
start = time.time()

#function to calculate sum of digits
def power_sum(n):
    add = 0 #variable to store the addition
    x = str(int(math.pow(2,n)))
    for i in range(0,len(x)):
        add += int(x[i])

    return add

print(power_sum(1000))
end = time.time()
print(end-start)
