#Self powers

import time
start = time.time()

add = 0

for num in xrange(1,1001):
    add += pow(num,num)

#print(add)

#convert the add into string
add = str(add)

#variable to store last 10 digits
s = ''

#print the last 10 digits
for i in xrange((len(add)-1), (len(add)-11), -1):
    s += add[i]

end = time.time()

print(s[::-1])
print(end - start)
