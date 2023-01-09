import time

start=time.time()
#The sum of the series upto 10**10 is already given
number=10405071317
#Loop to exponent and add the numbers
for i in range(11,1001):
    number+=i**i

#Convert to string and return last 10 digits
print(str(number)[-10:])
end=time.time()
print("Time Taken: ",end-start)
