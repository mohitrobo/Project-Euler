#Consecutive prime sum

#list to store prime number
prime = [2]

#dictionary to store the number of prime sum for a given prime
prime_sum = {}

num=2

#check for the length of prime list
y = 0

#function to find prime number
def prime_number(p):
    for i in range(2,p):
        if (p%i) == 0:
            break
    else:
        return True

#prime number upto 1000
for num in range(3,1000):
    if prime_number(num):
        prime.append(num)
        z = len(prime)
        x = prime[-1]
        for j in range(0,z-2):
            add = 0
            count = 0
            for k in range(j,z-1):
                add += prime[k]
                count += 1
                if add > x:
                    break
                elif add == x:
                    prime_sum[x] = count
        

maximum = max(prime_sum.values())
print(maximum)

#program to find key from values in dictionary
for k,v in prime_sum.items():
    if v == maximum:
        print(k)

        















