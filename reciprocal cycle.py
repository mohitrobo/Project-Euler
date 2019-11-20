#Reciprocal cycles

import time
start = time.time()

#function to find reciprocal digits
def reciprocal(n,d,p):
    remainder = set()
    for i in range(p):  #the maximum division used is the value od the denominator
        if n<d:
            n = n*10
        n = n%d
        if n in remainder:
            return (d,i)
        else:
            remainder.add(n)
        
        
longest = [0,0] #for comparison of the length

for x in range(2,1001):
    y = reciprocal(1,x,x)
    
    #check for length and compare with longest
    if y[1]>longest[1]:
        longest = y

print("The value 1/{} has the reciprocal cycle length of {}".format(longest[0],longest[1]))
end = time.time()
print(end-start)
