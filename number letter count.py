#Number letter counts from 1 to 1000

import time
start = time.time()

#create dictionary that stores value for the number
letter_dict = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,
               8:5,9:4,10:3,11:6,12:6,13:8,
               14:8,15:7,16:7,17:9,18:8,
               19:8,20:6,30:6,40:5,50:5,
               60:5,70:7,80:6,90:6,
               1000:11}


for i in xrange(21,100):
    tens = int(i/10)*10
    ones = i-tens
    letter_dict[i] = letter_dict[tens] + letter_dict[ones]

for i in xrange(100,1000):
    hundreds = int(i/100)
    tens = i - hundreds*100
    if tens == 0:
        letter_dict[i] = letter_dict[hundreds] + 7
    else:
        letter_dict[i] = letter_dict[hundreds] + letter_dict[tens] + 10

end = time.time()
print(sum(letter_dict.values()))
print(end-start)
