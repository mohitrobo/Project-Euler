#Digit fifth power

#let's assume the upper bound number be n = k*(9^5)
#so the possible upper bound number could be in the range
# 10^(k-1) <= k*(9^5) <= 10^(k)
#so we find that k = 6

import time
start = time.time()

add = 0 #for adding the numbers
for i in range(10,6*(9**5)):
    if sum([int(j)**5 for j in str(i)]) == i:
        add += i
        
end = time.time()
print(add)
print(end-start)
