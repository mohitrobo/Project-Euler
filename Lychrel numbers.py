#Lychrel numbers

import time

start = time.time()

#1. start numbering from 10 upto 10000
#2. convert into string
#3. reverse the string, convert into int and add to the number
#4. check if palindrome for 50 iterations
#5. if palindrome break the loop and stop doing the iterations
#5. if not palindrome, append into the list


count = 0

for num in xrange(10,10000):
    for i in xrange(1,51):
        s = str(num)
        p = str(num + int(s[::-1])) #addition of num and its reverse
        if p == p[::-1]:
            break
        else:
            if i==50:
                count += 1

        num = int(p)

print(count)

end = time.time()
print(end - start)
    
