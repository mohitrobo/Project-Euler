#XOR decryption
#The key length is 3
#The key is repeated cyclically throughout the message 


import time
from collections import Counter
import pdb

start = time.time()


import urllib2
data = urllib2.urlopen('https://projecteuler.net/project/resources/p059_cipher.txt')
#empty list to store the data
x = []
for i in data:
    x.append(i)
#store the data of x as a list of string
#there is only index 0 that is present in x
y = x[0].split(',')

pdb.set_trace()

#1.since key is repeated cyclically after every 3rd character
#the first character of the key is found by XOR of 1st,4th,7th,...element of encrypted message
#2. to find 2nd character of key, XOR with 2nd,5th,8th,...
#3. to find 3rd character of key, XOR with 3rd,6th,9th,...
#4. store every possible key in three different set i.e for 1st,2nd,3rd


#list to store ascii value of the possible plain message
letters = range(97,123)


first_letter = []

for i in xrange(0,len(y),3):
    for j in xrange(0,len(letters)):
        secret1 = int(y[i])^letters[j]
        if (32 <= secret1 <= 90) or (97 <= secret1 <= 122):
            first_letter.append(chr(letters[j]))

print(Counter(first_letter))

second_letter = []

for i in xrange(1,len(y),3):
    for j in xrange(0,len(letters)):
        secret2 = int(y[i])^letters[j]
        if (32 <= secret2 <= 90) or (97 <= secret2 <= 122):
            second_letter.append(chr(letters[j]))

print(Counter(second_letter))

third_letter = []

for i in xrange(2,len(y),3):
    for j in xrange(0,len(letters)):
        secret3 = int(y[i])^letters[j]
        if (32 <= secret3 <= 90) or (97 <= secret3 <= 122):
            third_letter.append(chr(letters[j]))


print(Counter(third_letter))


secret = []

for i in xrange(0,len(y)):
    a = int(y[i])^32
    if 97 <= a <= 122:
        secret.append(chr(int(y[i])^32))

print(Counter(secret))




            
        
