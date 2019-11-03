#Distinct powers

#to calculate a^b
#store in a list
#sort the list
#make it a set


distinct_power = []

for a in range(2,6):
    for b in range(2,6):
        distinct_power.append(pow(a,b))


#create set of unique elements and sort it
list_sort = sorted(set(distinct_power))

print("The list of values for a^b: {}".format(list_sort))
