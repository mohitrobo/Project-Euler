#Pandigital products
import time
start = time.time()

#for storing the product sum
products = set()

#Digits to be checked
digit = set('123456789')

#for single digit multiplicand
for a in xrange(1,10):  # a = 1 to 9
    for b in xrange(999,9999):
        s = str(a)+str(b)+str(a*b)
        if set(s) == digit:
            products.add(a*b)
        elif len(s)>9:
            break


#for double digit multiplicand
for a in xrange(10,99):  # a=10 to 99
    for b in xrange(99,999):
        s = str(a)+str(b)+str(a*b)
        if set(s) == digit:
            products.add(a*b)
        elif len(s)>9:
            break


print(sum(products))

end = time.time()
print(end-start)
