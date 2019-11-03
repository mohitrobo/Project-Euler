#Permuted multiples

#1. use while loop to increment the number
#2. as soon as the the number is obtained exit the loop
#3. multiply the number with 2,3,4,5,6
#4. convert the numbers into string
#5. sort the numbers and compare using 'and' operation

import time

start = time.time()

flag = True
num = 10 #starting with number 10

while flag:
    if sorted(str(num))==sorted(str(2*num))==sorted(str(3*num))==sorted(str(4*num))==sorted(str(5*num))==sorted(str(6*num)):
        flag = False
        print(num)
    num += 1


end = time.time()
print(end - start)
    
