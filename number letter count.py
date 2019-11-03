#Number letter counts from 1 to 1000


#function for values less 10
def less_ten(num):
    return letter_dict[num]
    

#function for values >= 10 and < 21
def less_twentyone(num1):
    return letter_dict[num1]
    

#function for value >= 21 and < 100
def less_hundred(num3):
    y = str(num3)  #string
    a = int(y[1])
    if y[0]=='2': 
        return letter_dict[20] + letter_dict[a]
    if y[0]=='3':
        return letter_dict[30] + letter_dict[a]
    if y[0]=='4':
        return letter_dict[40] + letter_dict[a]
    if y[0]=='5':
        return letter_dict[50] + letter_dict[a]
    if y[0]=='6':
        return letter_dict[60] + letter_dict[a]
    if y[0]=='7':
        return letter_dict[70] + letter_dict[a]
    if y[0]=='8':
        return letter_dict[80] + letter_dict[a]
    else:
        return letter_dict[90] + letter_dict[a]



#function check for value >= 100
def check_hundred(num4):
    if num4[0] == '0':
        return letter_dict[int(num4[1])]
    elif num4[0] == '1':
        c = less_twentyone(int(num4))
        return c
    else :
        c = less_hundred(int(num4))
        return c




#function for >= 100 and <1000
def less_thousand(num5):
    z = str(num5)  #string
    b = check_hundred(z[1:3])
    if z[0] == '1':
        return letter_dict[1]+letter_dict[100] + 3 + b #and = 3
    elif z[0] == '2':
        return letter_dict[2]+letter_dict[100] + 3 + b
    elif z[0] == '3':
        return letter_dict[3]+letter_dict[100] + 3 + b
    elif z[0] == '4':
        return letter_dict[4]+letter_dict[100] + 3 + b
    elif z[0] == '5':
        return letter_dict[5]+letter_dict[100] + 3 + b
    elif z[0] == '6':
        return letter_dict[6]+letter_dict[100] + 3 + b
    elif z[0] == '7':
        return letter_dict[7]+letter_dict[100] + 3 + b
    elif z[0] == '8':
        return letter_dict[8]+letter_dict[100] + 3 + b
    elif z[0] == '9':
        return letter_dict[9]+letter_dict[100] + 3 + b
        


#variable to store addition of letters
add = 0


#create dictionary that stores value for the number
letter_dict = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,
               8:5,9:4,10:3,11:6,12:6,13:8,
               14:8,15:7,16:7,17:9,18:8,
               19:8,20:6,30:6,40:5,50:5,
               60:5,70:7,80:6,90:6,100:7,
               1000:11}


for i in range(1,1000):
    if i<10:
        m = less_ten(i)
        add += m
    elif i>=10 and i<21:
        n = less_twentyone(i)
        add += n
    elif i>=21 and i<100:
        p = less_hundred(i)
        add += p
    else :
        q = less_thousand(i)
        add += q

print(add)
    










        
        
                               
               
