#Highly divisible triangular number
#find factors


def triangular(factors):
    
    #variable to check the while loop
    check = True

    #num for which factor is to be calculated
    num = 1
    #integer that is to be added to above number
    x = 1

    #loop for the operation
    while check:

        #empty list to store the factors
        factor_list = []

        for i in range(2,num+1):
            if num%i == 0:
                factor_list.append(i)
    
        #check for the length of the list
        if len(factor_list) == factors:
            check = False
            print(factor_list)
            print(num)
        else:
            x += 1
            num += x


divisor = int(input("Enter the number of divisor: "))
triangular(divisor)

    
