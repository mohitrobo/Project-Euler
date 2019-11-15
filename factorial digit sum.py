#factorial of number and sum of the digits in number
#in order to see how factorial is calculated go to program "factorial of number"

import math
import time
start = time.time()

fact = math.factorial(100)

#convert factorial value into string
s_fact = str(fact)
sum_fact = 0
for i in range(0,len(s_fact)):
    sum_fact += int(s_fact[i])

end = time.time()    
print(sum_fact)
print(end-start)
