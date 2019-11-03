#sum of the digits obtained from 2^value

import math

#function to calculate sum of digits
def power_sum(n):
    add = 0 #variable to store the addition
    x = str(int(math.pow(2,n)))
    for i in range(0,len(x)):
        add += int(x[i])

    return add


exponent = int(input("Enter the exponent: "))
print(power_sum(exponent))
