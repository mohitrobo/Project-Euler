#Distinct powers

#to calculate a^b
#store in a list
#sort the list
#make it a set

import time
start = time.time()

distinct_power = []

for a in range(2,101):
    for b in range(2,101):
        distinct_power.append(pow(a,b))


#create set of unique elements and sort it
list_sort = sorted(set(distinct_power))

print("The list of values for a^b: {}".format(len(list_sort)))
end = time.time()
print(end-start)
