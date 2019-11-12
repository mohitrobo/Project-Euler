#Longest Collatz sequence

import time
start = time.time()

#function for collatz sequence
def collatz(num):
    #variable for length of sequence
    length = 0
    #check if even or odd and continue the loop until the number=1
    check = True
    while check:
        if num%2 == 0: #even
            num = num/2
            length += 1
            if num==1:
                check = False
        else: #odd
            num = 3*num+1
            length += 1
            if num==1:
                check = False

    return length

#variable for length of sequence for comparison
compare = 0
#variable for storing the number and the count
coll,coll_len = 0,0
#loop for number
for number in xrange(13,1000000):
    count = collatz(number)
    if count>compare:
        compare = count
        coll,coll_len = number,count


end = time.time()
print(coll,coll_len)
print(end-start)
        
