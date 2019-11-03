#program to find the largest prime factor of a number

#Enter the number for which prime factor needs to be found
num = int(input("Enter the number: "))

#empty list for storing prime factors
prime_factor = []

lower = 2
upper = 100000

#for finding and incrementing the prime factors
for x in range(lower, upper+1):
    if x > 1:
        for i in range(2,x):
            if (x%i) == 0:
                break

        #Once prime factor is found
        else:
            #while loop to check if the same prime factor can do the division
            while(num%x == 0): 
                prime_factor.append(x)
                num = num//x

    #Once the quotient obtained is 1
    if num == 1:
        break

print(prime_factor)
print(max(prime_factor))

