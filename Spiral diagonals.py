#Number Spiral Diagonals

import time
start = time.time()

#function to calculate sum
def spiral(n):
    sum_diag = 0 #variable to store sum of diagonals

    j = 1 #for even section
    k = 1 #for odd section
    
    for i in range(1,n+1):

        #condition for i = 1
        if i==1:
            sum_diag += (i*i)

        #condition to check even
        elif i%2 == 0:
            x = (i*i)+1
            sum_diag += x
            sum_diag += (x + (2*j))
            j += 1

        else:  #odd for values >= 3
            y = i*i
            sum_diag += y
            sum_diag += (y - (6*k))
            k += 1

    return (sum_diag)

print("The summation of diagonal elements of spiral matrix: {}".format(spiral(1001)))
end = time.time()
print(end-start)
