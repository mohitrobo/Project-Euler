#Champernowne's constant

#1.) I need the fractional part with numbers starting from 1 to 1000000 number
#2.) Since we need to retrieve the digit locations and multiply them, so we do not need to iterate till 1000000 number
#3.) So we need to find the number to iterate through so that the number of digits reaches 1000000
#4.) We know that there are 9--->1 digit numbers--> 9*1 digits
#                 there are 90--->2 digit numbers--> 90*2 digits
#                 there are 900--->3 digit numbers--> 900*3 digits
#                 there are 9000--->4 digit numbers--> 9000*4 digits
#                 there are 90000--->5 digit numbers--> 90000*5 digits
#                 there are 900000--->6 digit numbers--> 900000*6 digits

# Calculation 9*1+90*2+900*3+9000*4+90000*5+900000*6=5888889 digits
# 5888889>1000000
# 9*1+90*2+900*3+9000*4+90000*5+n*6=1000000 digits-----> the value of n~85186

# Therefore, the total number of iteration will:-
#   9+90+900+9000+90000+85186=185185(including the last value 185185)

# Import time library
import time

start=time.time()
#String to store the digits as string
s=''
for i in range(1,185186):
    #Append the digits as string to the string s
    s=s+str(i)
    i+=1


d1=int(s[0])
d10=int(s[9])
d100=int(s[99])
d1000=int(s[999])
d10000=int(s[9999])
d100000=int(s[99999])
d1000000=int(s[999999])
    
print(d1*d10*d100*d1000*d10000*d100000*d1000000)
print("Execution time= ",time.time()-start)



# The answer is 210
# Execution time:- 0.1579587459564209
