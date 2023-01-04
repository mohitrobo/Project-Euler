#1.) You do not need to find the list of pentagon numbers
#2.) You just have to check whether the difference and sum of pentagon numbers is also a pentagon number
#3.) (P_k-P_j) and (P_k+P_j) is a pentagon number---> check
#4.) Define a function if the sum and difference of pentagon number is also pentagon number
#5.) P_n=n*(3n-1)/2-----> on rearranging the value of n=(1+sqrt(1+24*P_n))/6
#6.) The value of n should be an integer therefore, (1+sqrt(1+24*P_n))%6==0

import time
from math import sqrt

#Function to check if pentagonal number
#Here P needs to be pentagonal number
def is_pentagonal(P):
    return (1+sqrt(1+24*P))%6==0
  
  
start=time.time()
flag=True
k=1
while flag:
    for j in range(1,k):
        P_k=(k*(3*k-1))//2
        P_j=(j*(3*j-1))//2
        #Check the difference and sum if pentagonal
        if is_pentagonal(P_k-P_j) and is_pentagonal(P_k+P_j):
            #Print the value of D=P_k-P_j
            print("The minimum number is: ",P_k-P_j)
            flag=False
            #break from the for loop
            break
            
    k+=1
end=time.time()
print("Time taken: ",end-start)
