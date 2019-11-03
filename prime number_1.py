#what is the 10001st prime number

#lowest prime number
lower = 3

#empty list to store prime number
prime_list = [2]

#condition for while loop
check = True

while check:
    if lower>1:
        for i in range(2,lower):
            if (lower%i) == 0:
                break
        else:
            prime_list.append(lower)
            if prime_list.index(lower) == 10000:
                check = False
                print("The 10001th prime number: {}".format(lower))
                break

    lower +=2

#print(prime_list)
