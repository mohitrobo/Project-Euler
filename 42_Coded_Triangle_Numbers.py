#1.) First import the file and check it's datatype
#    a.) the datatype is bytes
#    b.) convert bytes to string using .decode()
#2.) Convert string to list using split(,)
#3.) Remove inverted commas(") from each element of the list

import time
import string
import urllib.request as urllib2  # the lib that handles the url stuff


my_text = urllib2.urlopen("https://projecteuler.net/project/resources/p042_words.txt").read()

start=time.time()
#Convert byte to string
my_text=my_text.decode()

#Store the string into list using split method
my_list = my_text.split(",")

#Remove inverted commas from each element of the list
new_list = [item.replace('"', '') for item in my_list]



#4.) Now we need to create a list of triangle numbers but we do not know upto what values.
#5.) The task is asking to check if the addition of alphabet positions leads to triangle number
#6.) The maximum possible triangle number can be obtained is by first finding the maximum length of the string in the list
#7.) We need to find the maximum length of the string in the list
#Length of strings of the list
#length_string=[len(item) for item in new_list]
#max(length_string)#---->14

#8.) The maximum length obtained is 14--->maximum possible value of triangle number will be zzz..z--->14 times---->26*14=364
#9.) Using the triangle number formula 0.5*n*(n+1)=364, find the approximate maximum value of n(for iteration)
#10.) Using the string library, fetch the alphabet position values, 
#     add them and check if the number obtained is in triangle number list


#Store triangle numbers in a list
triangle_number=[int(0.5*n*(n+1)) for n in range(1,28)]

#Store the alphabet string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet=string.ascii_uppercase

#create a variable that stores the count
count=0
#Iterate through the list containing string
for s in new_list:
    #create a variable that stores the addition of the alphabet positions
    add_check=0
    #iterate alphabet by alphabet of each string
    for alpha in s:
        add_check+=alphabet.find(alpha)+1
    
    #check if the added value is in triangle_number list
    if add_check in triangle_number:
        count+=1
        
print(count)

end=time.time()
print('Time taken: ',end-start)


