#counting sundays

#create a dictionary to store week
week = ['sun','mon','tue','wed','thur','fri','sat']

#list to store 3 days in january
sun_jan = ['tue','wed','thur'] #for year 1901

#variable to store number of sundays of january
sun_year = 4  #for year 1901

i = 2

#variable to find the 1st january of a year
first_jan = ""


for year in range(1902,2001):
    if (year-1)%4 == 0:
        if (i+2)>=7:
            i = i-5
            first_jan = week[i]
        else:
            i = i+2
            first_jan = week[i]

    else:
        if (i+1)==7:
            i = i-7
            first_jan = week[i]
        else:
            i = i+1
            first_jan = week[i]

    #52 sundays to be added every year
    sun_year += 4

    j = week.index(first_jan)

    #store 3 remaining days in january
    for n in range(j,j+3):
        sun_jan.append(week[n-7])  


#count number of sundays in the list
x = sun_jan.count('tue')
print(x)
sun_year += x
print(sun_year)














    

