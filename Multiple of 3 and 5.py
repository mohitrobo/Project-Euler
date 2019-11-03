#multiple of 3 or 5 and add the numbers

#ask for the maximum number upto which condition is to be checked
num = int(input("enter the number: "))
num_sum = 0 #for storing the addition of numbers

for x in range(num):
    if (x%3 == 0) or (x%5 == 0):
        num_sum += x
    else:
        pass

print("The total sum is: {}".format(num_sum))
