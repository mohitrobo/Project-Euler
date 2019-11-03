#to find the prime factors of a number

def prime_factor(x):

    for i in range(2,x+1):
        if x%i == 0:
            print(i)

num = int(input("Enter the number: "))

prime_factor(num)
