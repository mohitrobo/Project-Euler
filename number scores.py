#Names Scores

#List of names
name_list = ['rohan','mohan','jack','raju','pankaj','rajiv','ravinder','rajesh','jose','yash']
sort_name = sorted(name_list)
print(sorted(name_list))

#dictionary to store alphabet values
alphabet_value = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,
                  'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
                  'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,
                  'z':26}



#list to store multiplied values
multiply_value = []

#loop for accessing the alphabet values
for i in range(0,len(sort_name)):
    add_name = 0
    position = i+1
    for j in range(0,len(sort_name[i])):
        add_name += alphabet_value[sort_name[i][j]]
        
    multiply_value.append(position*add_name)

print(multiply_value)
    
        
