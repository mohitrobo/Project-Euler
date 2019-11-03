#Coded triangle numbers


import math
import urllib
import time

start = time.time()

opener = urllib.FancyURLopener({})
f = opener.open("https://projecteuler.net/project/resources/p042_words.txt")
lines = f.read()
new = lines.split('","')




#make a dictionary of alphabets
alpha = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11
         ,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20
         ,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}



#function to check triangle number
def triangle(num):
    a = 1
    b = 1
    c = -2*num
    #discriminant
    d = pow(b,2)-4*a*c
    if d >= 0:
        n1 = ((-b)+math.sqrt(d))/(2*a)
        n2 = ((-b)-math.sqrt(d))/(2*a)
        if n1>0 and n2<0:
            y = math.modf(n1)
            if y[0] == 0: #no decimal part present
                return True
            else:
                return False
        elif n2>0 and n1<0:
            y = math.modf(n2)
            if y[0] == 0: #no decimal part present
                return True
            else:
                return False
        elif n1>0 and n2>0:
            y1 = math.modf(n1)
            y2 = math.modf(n2)
            if y1[0]==0 or y2[0]==0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
            
    


#list to store triangle words
words = []

#variable to count the words that are coded triangle numbers
counter = 0

for i in xrange(0,len(new)):
    #variable for addition
    x = 0
    if i == 0:
        for j in xrange(1,len(new[i])):
            x += alpha[new[i][j]]
        z = triangle(x)
        if z:
            #words.append(new[i])
            counter += 1
            
    elif i == len(new)-1:
        for j in xrange(0,len(new[i])-1):
            x += alpha[new[i][j]]
        z = triangle(x)
        if z:
            #words.append(new[i])
            counter += 1
    else:
        for j in xrange(0,len(new[i])):
            x += alpha[new[i][j]]
        z = triangle(x)
        if z:
            #words.append(new[i])
            counter += 1


end = time.time()

print(counter)
print(end - start)
