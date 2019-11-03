#maximum path sum

import numpy as np

x = np.array([[3],[7,4],[2,4,6],[8,5,9,3]])


#i=rows and j=columns

for i in range(len(x) - 2, -1, -1): #bottom to top
    for j in range(0,i+1): #within the same row column is changed
        if x[i+1][j] > x[i+1][j+1]:
            x[i][j] += x[i+1][j]
        else:
            x[i][j] += x[i+1][j+1]

print(x[0][0])
        
