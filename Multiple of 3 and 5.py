#multiple of 3 or 5 and add the numbers
import time
start = time.time()

num_sum = 0 #for storing the addition of numbers
for x in xrange(1000):
    if (x%3 == 0) or (x%5 == 0):
        num_sum += x

print("The total sum is: {}".format(num_sum))
end = time.time()
print(end-start)
