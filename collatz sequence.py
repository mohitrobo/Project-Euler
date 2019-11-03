#Longest Collatz sequence

#function to find collatz sequence
def collatz(num):
    #while loop check
    check = True

    #empty list to store sequence
    coll_seq = [num]
    
    while check:
        if num%2==0:  #check even number
            num = num/2
            coll_seq.append(num)
            if num==1:
                check = False
                return coll_seq
        else:  #odd number
            num = 3*num + 1
            coll_seq.append(num)
            if num==1:
                check = False
                return coll_seq





number = int(input("Enter the number for which collatz sequence is to be found: "))
sequence = collatz(number)
print(sequence)
