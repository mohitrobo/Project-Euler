#calculate factorial of a number

#function to calculate factorial
def factorial(num):
    product = 1
    for i in xrange(num,0,-1):
        product *= i

    return product


number = int(input("Enter the number for which factorial is to be calculated: "))
print(factorial(number))
