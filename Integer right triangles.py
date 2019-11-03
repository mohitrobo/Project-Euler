#Integer right triangles (Problem 39)
#perimeter <= 100 with maximum number of solutions
#a,b,c are taken
#a = (1,299) and b = (1,299) and c = hypotenuse

from collections import Counter  #for counting the number of occurances of perimeter value



#dictionary to store perimeter and number of occurances
perimeter = []

#list to store perimeter values
peri = []

for a in xrange(1,500):  
    for b in xrange(1,500):
        c = pow((pow(a,2)+pow(b,2)) , 0.5)
        p = a+b+c  #p is perimeter which is a key for dictionary
        if p <= 1000:
            peri.append(p)


count = Counter(peri)  #this creates a dictionary

print(count.most_common(1)[0])

###################################
OR YOU CAN DO IT BY ANOTHER WAY
###################################


#max_occur = max(count.values())  #max of all values

#convert the dictionary into list of tuples
#count_tuple = count.items()

#loop to check for the max value
#for item in count_tuple:
 #   if item[1] == max_occur:
  #      perimeter.append(item)


#print(perimeter)
            
