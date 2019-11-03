#smallest positive number divisible by all numbers from 1 to 20
# as we know that the smallest positive number divisible by numbers 1 to 10 is 2520, so we will start from 2520

#starting number
num = 232792500

#condition to remain in while loop
check = True

while check:
    num +=1
    #list to check for boolean value
    check_list = [0]

    for x in range(2,21):  #check division by numbers
        check_list.append(bool(num%x))

        #check if any element in list is True
        if any(check_list):
            break  #breaks from for loop
        elif x==20: #all values in list turns out to be false
            check = False

print(num)
            
