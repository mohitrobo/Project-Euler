#1000 digit fibonacci number

#for measuring the total time taken to execute
import time 

start = time.time()

L = [1,1]
a,b = L

check = True
while check:
    L.append(a+b)
    x = str(a+b)
    if len(x) == 1000:
        check = False
        L_index = L.index(a+b)
    
    a,b = b,a+b

print("The index of the 1000 digit number is : {}".format(L_index+1))

end = time.time()
print(end-start)

    
    
