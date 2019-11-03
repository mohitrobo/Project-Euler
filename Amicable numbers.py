#to find the prime factors of a number
#Amicable numbers

def prime_factor(x):
    amicable_sum = 0
    for i in range(1,x):
        if x%i == 0:
            amicable_sum += i

    return amicable_sum

#num = int(input("Enter the number: "))

#list to store amicable numbers
amicable_list = []


#search amicable numbers within 1000
for i in range(1,10000):
    x_sum = prime_factor(i)
    y_sum = prime_factor(x_sum)
    if i == y_sum:
        if x_sum != y_sum:
            amicable_list.append(i)
            amicable_list.append(x_sum)
        else:
            pass
    else:
        pass

#unique numbers within the list
unique_list = set(amicable_list)

print(unique_list)

#convert set into list as set doesn't support indexing
list_set = list(unique_list)

#sum of all amicable numbers
unique_sum = 0
for j in range(0,len(list_set)):
    unique_sum += list_set[j]


print("The sum of the unique amicable numbers: {}".format(unique_sum))
