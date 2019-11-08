#The smallest number divisible by a set of numbers is known as LCM of set of numbers
# Hence LCM(k1, k2, ..., k_m) = LCM(...(LCM(LCM(k1, k2), k3)...), k_m).
from fractions import gcd
import time

start1 = time.time()

#variable for storing the LCM of numbers
lcm = 1
for x in xrange(1,21):
    lcm *= x/gcd(x,lcm)
print(lcm)
end1 = time.time()
print(end1-start1)
