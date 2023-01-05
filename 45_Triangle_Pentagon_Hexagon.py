#1.) You do not need to find the list of pentagon and hexagon numbers 
#2.) You just have to check whether the triangle number(starting from n=286) is pentagon and hexagon number
#3.) P_n=n*(3n-1)/2-----> on rearranging the value of n=(1+sqrt(1+24*P_n))/6
#4.) The value of n should be an integer therefore, (1+sqrt(1+24*P_n))%6==0
#5.) H_n=n*(2n-1)----> on rearranging the value of n=(1+sqrt(1+8*H_n))/4
#6.) The value of n should be an integer therefore, (1+sqrt(1+8*H_n))%4==0


import time
from math import sqrt

#Function to check if pentagonal and hexagonal number
#Here P needs to be pentagonal and hexagonal number
def is_pent_hex(P):
    return (1+sqrt(1+24*P))%6==0 and (1+sqrt(1+8*P))%4==0
  

start=time.time()
flag=True

#start from i=286
i=286
while flag:
    #find the triangle number
    T=i*(i+1)//2
    #check for pentagonal and hexagonal number
    if is_pent_hex(T):
        print(T)
        flag=False
        
    i+=1
    
end=time.time()
print('Time taken: ',end-start)
