#Largest palindrome made from the product of two 3 digit numbers

#store the palindrome values in an empty list
palin_list = []

#multiplication of two 3 digit values in variable a and b
for a in range(100,1000):
    for b in range(100,1000):
        num = str(a*b)  #convert multiplication into string so as to access the index value for comparison among index
        num_length = len(num)
        i = 0 #for index
        j = num_length - 1 #for index

        #comparison happens here
        while (num[i] == num[j]):
            i += 1 #incrementing the index from start
            j -= 1 #decrementing the index from last

            #check whether middle index has been reached
            if i == round(num_length / 2):
                palin_list.append(int(num)) #value is converted back to int
                break

print(max(palin_list))

        
