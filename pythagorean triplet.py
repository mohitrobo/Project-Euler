#calculate pythagorean triplet and sum of the number=1000
#a<b<c


def pythagorean():
    for a in range(500):
        for b in range(a+1,500):
            c = 1000 - (a+b)
            if a**2 + b**2 == c**2:
                print("the numbers are {},{},{}".format(a,b,c))
                return a*b*c

product = pythagorean()
print(product)
