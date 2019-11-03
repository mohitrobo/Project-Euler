#Distinct Prime Factors

#function to find prime factors and return the set length
#program taken from Largest prime factor
def prime_factor(number):
    #list to store factor
    factor = []
    x = 2
    check = True
    while check:
        for i in xrange(2,x):
            if (x%i) == 0:
                break
        else:
            #while loop to check if the same prime factor can do the division
            while (number%x == 0):
                factor.append(x)
                number = number//x

        if number == 1:
            check = False

        x += 1

    return (len(set(factor)))


#print(prime_factor(644))

#create a while loop to increment the number
#as soon as 4 consecutive number with 4 prime factors are obtained move out of loop
#start with number 646 as it is given in question itself


#variable to store the highest number that is part of consecutive number
consecutive = 0

num = 100000
flag = True

while flag:
    if prime_factor(num) == 4:
        num += 1
        if prime_factor(num) == 4:
            num += 1
            if prime_factor(num) == 4:
                num += 1
                if prime_factor(num) == 4:
                    consecutive = num
                    flag = False
    num += 1



for j in xrange(3,-1,-1):
    print(consecutive-j)









        









    
    
