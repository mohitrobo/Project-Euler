#Digit fifth power
#problem 30 of project euler



#list to store digit 5th power
digit_power = []

for i in range(10,354394):
    total = 0
    for j in str(i):
        total += pow(int(j),5)
    if total == i:
        digit_power.append(i)

print(digit_power)
        
